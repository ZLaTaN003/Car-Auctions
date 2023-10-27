from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass



   

class AuctionListing(models.Model):
    theuser = models.ForeignKey(User,on_delete = models.CASCADE,related_name='theuser')
    title = models.CharField(max_length=400)
    description = models.TextField()
    item_img = models.ImageField(default='pictures/placehold.jpg',upload_to='pictures')    
    date_created = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2)  

    category = models.CharField(max_length=250,null=True)

    active = models.BooleanField(default=True)
    
    watchlist = models.ManyToManyField(User,blank=True,related_name='watchlist')

    def __str__(self):
        return f"{self.theuser} sells {self.title}"



class Bid(models.Model):
    bid_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bider')
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    auction = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name='bids')

    def __str__(self):
        return f"{self.bid_user} bids {self.bid_amount} "


class Comments(models.Model):
    commentor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='commentor')
    comment = models.TextField()
    auction = models.ForeignKey(AuctionListing,on_delete=models.CASCADE,related_name='auction_comment')
    date_created = models.DateTimeField(default=timezone.now,null=True,blank=True)
    


    def __str__(self):
        return f"{self.commentor} says{self.comment} "