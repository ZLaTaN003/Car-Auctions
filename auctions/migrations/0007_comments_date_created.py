# Generated by Django 4.2.3 on 2023-10-19 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auctionlisting_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
