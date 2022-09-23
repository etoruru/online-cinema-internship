from django.db import models


class Person(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    picture = models.CharField(max_length=200)
