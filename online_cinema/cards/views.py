from rest_framework import viewsets

from .models import Card, Episode, Season
from .serializers import (
    CardCreateSerializer,
    CardListSerializer,
    CardSerializer,
    EpisodeCreateSerializer,
    EpisodeListSerializer,
    EpisodeSerializer,
    SeasonListSerializer,
    SeasonSerializer,
)


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return CardListSerializer
        elif self.action == "create":
            return CardCreateSerializer
        return CardSerializer

    def perform_create(self, serializer):
        serializer.save(
            country=self.request.data["country"], genres=self.request.data["genres"]
        )


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
        elif self.action == "create":
            return EpisodeCreateSerializer
        return EpisodeSerializer

    def perform_create(self, serializer):
        serializer.save(season=self.request.data["season"])
