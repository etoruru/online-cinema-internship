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


class Genres(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="genres")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="genres")


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
