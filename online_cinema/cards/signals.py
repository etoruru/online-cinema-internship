from cards.models import Card, Episode, Season
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


@receiver(post_save, sender=Card)
def cards_save_handle(sender, instance, created, **kwargs):
    if instance.type == "F":
        season = Season.objects.create(name="1", card=instance)
        Episode.objects.create(season=season)
    elif instance.type == "S":
        Season.objects.create(name="1", card=instance)
