from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User,AuctionListing,Comments,Bid
from .forms import AuctionForm,BidForm



def index(request):
    auction_list = AuctionListing.objects.filter(active=True)
    return render(request, "auctions/homie.html",{
        'auction_list' : auction_list
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create(request):
    if request.method == "POST":
     form = AuctionForm(request.POST,request.FILES)
     if form.is_valid():
         form = form.save(commit=False)
         form.theuser = request.user
         form.save()
         return HttpResponseRedirect(reverse("index"))
    else:
     form = AuctionForm()
    return render(request,'auctions/create.html',
                  {'form': form})


def listing_details(request,id):
    auction = AuctionListing.objects.get(pk=id)
    inwatch = request.user in auction.watchlist.all()
    mycomments = Comments.objects.filter(auction=auction)
    bidform =BidForm()
    error = None
    winner_message = None
    iscreator = request.user.username==auction.theuser.username
    highest_bid = auction.bids.order_by('-bid_amount').first()
    if not auction.active:
     if highest_bid.bid_user == request.user:
            winner_message = "Congratulations, you have Won this auction!"
     else:
            winner_message = f"The Winner of The Auction is {highest_bid.bid_user}."

    if request.method == "POST":
        bidform = BidForm(request.POST)
        if bidform.is_valid():
            bid_amount = bidform.cleaned_data['bid_amount']
            if bid_amount > auction.price:
                mybid = Bid(bid_user = request.user,bid_amount=bid_amount,auction=auction)
                mybid.save()
                auction.price = bid_amount
                auction.save()
            else:
                error = "Price must be Above Current bid"
    
    return render(request,'auctions/listing.html',{
        'auction': auction,
        'inwatch': inwatch,
        'mycomments': mycomments,
        'bid': bidform,
        'error': error,
        'iscreator': iscreator,
        'winner_message':  winner_message,
        'highest_bid': highest_bid

    })


def watchlist(request):
    auctions_watchs = request.user.watchlist.filter(active=True)
    
    return render(request,'auctions/watchlist.html',{'auctions_watchs':auctions_watchs,
                                                     })


def addwatch(request,id):
   auction  = AuctionListing.objects.get(pk=id)
   auction = auction.watchlist.add(request.user)
   return HttpResponseRedirect(reverse("listing_details", args=[id]))

def removewatch(request,id):
   auction  = AuctionListing.objects.get(pk=id)
   auction = auction.watchlist.remove(request.user)
   return HttpResponseRedirect(reverse("listing_details", args=[id]))





def removeitem(request,id):
    if request.method == "POST":
        auction  = AuctionListing.objects.get(pk=id)
        auction.active = False
        auction.save()
        return HttpResponseRedirect(reverse("index"))





def comment(request,id):
    auction = AuctionListing.objects.get(pk=id)
    com = request.POST['mycomment']

    mycom = Comments(commentor=request.user,comment=com,auction=auction)

    mycom.save()
   

    return HttpResponseRedirect(reverse("listing_details", args=[auction.id]))


def completed(request):
    completed = AuctionListing.objects.filter(active=False)
    return render(request,'auctions/completed.html',{'completed':completed})















def categories(request):

    if request.method == "POST":
        selected_category = request.POST.get('caty')
        if selected_category:
            auction_list = AuctionListing.objects.filter(category=selected_category, active=True)
        else:
            auction_list = AuctionListing.objects.filter(active=True)
    else:
        auction_list = AuctionListing.objects.filter(active=True)
    
    categories = AuctionListing.objects.values_list('category', flat=True).distinct()
    

    return render(request, 'auctions/categori.html', {
        'categories': categories,
        
        'auction_list': auction_list,
    })
