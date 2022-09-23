from django.db import models


class Season(models.Model):
    name = models.CharField(max_length=200)
    card = models.ForeignKey("Card", on_delete=models.CASCADE, related_name="seasons")
