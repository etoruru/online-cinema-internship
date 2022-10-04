from django.db import models
from django.utils.translation import gettext_lazy as _


class Card(models.Model):
    class CardType(models.TextChoices):
        FILM = "F", _("film")
        SERIES = "S", _("series")

    type = models.CharField(max_length=1, choices=CardType.choices)
    name = models.CharField(max_length=200)
    description = models.TextField()
    released_year = models.DateField()
    country = models.ForeignKey(
        "Country", on_delete=models.CASCADE, related_name="cards"
    )
    banner = models.CharField(max_length=200)
    is_available = models.BooleanField(default=False)
    cast = models.ManyToManyField("cast.Person", through="Membership")
    genres = models.ManyToManyField("Genre")


class Membership(models.Model):
    character = models.CharField(max_length=200)
    person = models.ForeignKey(
        "cast.Person", on_delete=models.CASCADE, related_name="card_to_person"
    )
    item = models.ForeignKey(
        "Card", on_delete=models.PROTECT, related_name="card_to_person"
    )
