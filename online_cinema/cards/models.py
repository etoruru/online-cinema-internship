from cast.models import Person
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)


class Genre(models.Model):
    name = models.CharField(max_length=200)


class Card(models.Model):
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
        Person, on_delete=models.CASCADE, related_name="membership"
    )
    item = models.ForeignKey(Card, on_delete=models.PROTECT, related_name="membership")


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
    viewers = models.IntegerField()
    updated_to = models.DateTimeField()
