from django.contrib import admin
from .models import Bid, Client, Admin, Auction

admin.site.register(Bid)
admin.site.register(Client)
admin.site.register(Admin)
admin.site.register(Auction)
