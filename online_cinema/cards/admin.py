from cards.models import Card, Country, Episode, Genre, Membership, Season
from django.contrib import admin

# Register your models here.
admin.site.register(Card)
admin.site.register(Season)
admin.site.register(Episode)
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Membership)
