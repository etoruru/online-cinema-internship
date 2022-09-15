from cast.models import Person
from django.db import models

CARD_TYPE = [("F", "film"), ("S", "series")]


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Card(models.Model):
    type = models.CharField(max_length=1, choices=CARD_TYPE)
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
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="cards")
    item = models.ForeignKey(Card, on_delete=models.PROTECT, related_name="cards")


class Season(models.Model):
    name = models.CharField(max_length=200)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="seasons")


class Episode(models.Model):
    season = models.ForeignKey(
        Season, on_delete=models.CASCADE, related_name="episodes"
    )
    num = models.IntegerField()
    name = models.CharField(max_length=200)
    preview = models.CharField(max_length=200)
    description = models.TextField()
    viewers = models.IntegerField(default=0)
    updated_to = models.DateTimeField()
