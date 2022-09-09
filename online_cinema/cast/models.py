from cards.models import Card
from django.db import models


class Person(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    picture = models.CharField(max_length=200)


class Cast(models.Model):
    character = models.CharField(max_length=200)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="cast")
    card = models.ForeignKey(Card, on_delete=models.PROTECT, related_name="cast")
