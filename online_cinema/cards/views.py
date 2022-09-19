from rest_framework import viewsets
from users.permissions import HasGroupPermission

from .models import Card, Episode, Season
from .serializers import (
    CardCreateSerializer,
    CardListSerializer,
    CardSerializer,
    EpisodeCreateSerializer,
    EpisodeListSerializer,
    EpisodeSerializer,
    SeasonCreateSerializer,
    SeasonListSerializer,
    SeasonSerializer,
)


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [HasGroupPermission]
    permission_groups = {
        "create": ["moderator", "admin"],
        "list": ["_Public"],
        "retrieve": ["_Public"],
        "partial_update": ["moderator", "admin"],
        "delete": ["admin"],
    }

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
    permission_classes = [HasGroupPermission]
    permission_groups = {
        "create": ["moderator", "admin"],
        "list": ["_Public"],
        "retrieve": ["_Public"],
        "partial_update": ["moderator", "admin"],
        "delete": ["admin"],
    }

    def get_serializer_class(self):
        if self.action == "list":
            return SeasonListSerializer
        elif self.action == "create":
            return SeasonCreateSerializer
        return SeasonSerializer


class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    permission_classes = [HasGroupPermission]
    permission_groups = {
        "create": ["moderator", "admin"],
        "list": ["_Public"],
        "retrieve": ["_Public"],
        "partial_update": ["moderator", "admin"],
        "delete": ["admin", "moderator"],
    }

    def get_serializer_class(self):
        if self.action == "list":
            return EpisodeListSerializer
        elif self.action == "create":
            return EpisodeCreateSerializer
        return EpisodeSerializer

    # def perform_create(self, serializer):
    #     serializer.save(season=self.request.data["season"])
