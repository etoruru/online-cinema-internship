from cast.models import Person
from django.db import models
from django.utils.translation import gettext_lazy as _

from .country import Country
from .genre import Genre


class Card(models.Model):
    class CardType(models.TextChoices):
        FILM = "F", _("film")
        SERIES = "S", _("series")

    type = models.CharField(max_length=1, choices=CardType.choices)
    name = models.CharField(max_length=200)
    description = models.TextField()
    released_year = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="cards")
    banner = models.CharField(max_length=200)
    is_available = models.BooleanField(default=False)
    cast = models.ManyToManyField(Person, through="Membership")
    genres = models.ManyToManyField(Genre)


class Membership(models.Model):
    character = models.CharField(max_length=200)
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="character"
    )
    item = models.ForeignKey(Card, on_delete=models.PROTECT, related_name="character")
