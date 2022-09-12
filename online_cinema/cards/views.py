from cards.models import Card, Episode, Season
from cards.serializers import (
    CardListSerializer,
    CardSerializer,
    EpisodeListSerializer,
    EpisodeSerializer,
    SeasonListSerializer,
    SeasonSerializer,
)
from rest_framework import viewsets


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return CardListSerializer
        return CardSerializer


class SeasonViewSet(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return SeasonListSerializer
        return SeasonSerializer


class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return EpisodeListSerializer
        return EpisodeSerializer
