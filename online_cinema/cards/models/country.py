from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = "cards"

    def __str__(self):
        return self.name
