from django.contrib import admin

from .models import Card, Country, Episode, Genre, Membership, Season

# Register your models here.
admin.site.register(Card)
admin.site.register(Season)
admin.site.register(Episode)
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Membership)
