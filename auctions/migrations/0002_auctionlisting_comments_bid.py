# Generated by Django 4.2.3 on 2023-10-18 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('img_url', models.CharField(max_length=800)),
                ('price', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('starting_bid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('active', models.BooleanField()),
                ('category', models.CharField(max_length=400)),
                ('theuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction_comment', to='auctions.auctionlisting')),
                ('commentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction_bid', to='auctions.auctionlisting')),
                ('bid_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
