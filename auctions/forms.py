from django import forms
from . import models



from django import forms
from . import models

CATEGORY_CHOICES = [
    ('Sedans', 'Sedan Cars Section'),
    ('SUVs', 'SUV Cars Section'),
    ('Sports', 'Sports Cars Section'),
    ('Luxury', 'Luxury Cars Section'),
    ('Electric', 'Electric Cars Section'),
    ('Trucks', 'Truck Section'),
    ('Vans', 'Van Cars Section'),
    ('Classic', 'Classic Cars Section'),
    ('Off-Road', 'Off-Road Cars Section'),
    ('Convertibles', 'Convertible Cars Section'),
    ('Coupes', 'Coupe Cars Section'),
    ('Compact Cars', 'Compact Cars Section'),
    ('Midsize Cars', 'Midsize Cars Section'),
    ('Full-Size Cars', 'Full-Size Cars Section'),
    ('Supercars', 'Supercars Section'),
    ('Vintage Cars', 'Vintage Cars Section'),
    ('Muscle Cars', 'Muscle Cars Section'),
    ('Hybrid Cars', 'Hybrid Cars Section'),
    ('Antique Cars', 'Antique Cars Section'),
    ('Exotic Cars', 'Exotic Cars Section'),
    ('Racing Cars', 'Racing Cars Section'),
]

class AuctionForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select)
    
    class Meta:
        model = models.AuctionListing
        fields = ['title', 'description', 'price', 'item_img', 'category']

class BidForm(forms.Form):
    bid_amount = forms.DecimalField(label='Bid Amount', max_digits=10, decimal_places=2)


class AuctionForm(forms.ModelForm):

 

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select)
    
    class Meta:
        model = models.AuctionListing
        fields = ['title', 'description', 'price', 'item_img',  'category']


class BidForm(forms.Form):
    bid_amount = forms.DecimalField(label='Bid Amount', max_digits=10, decimal_places=2)