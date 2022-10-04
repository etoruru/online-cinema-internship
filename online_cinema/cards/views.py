from django_filters import rest_framework as filters
from rest_framework import viewsets
from users.permissions import HasGroupPermission

from .models import Card, Country, Episode, Genre, Membership, Season
from .serializers import (
    CardCreateSerializer,
    CardListSerializer,
    CardSerializer,
    CountrySerializer,
    EpisodeCreateSerializer,
    EpisodeListSerializer,
    EpisodeSerializer,
    GenreSerializer,
    MembershipSerializer,
    SeasonCreateSerializer,
    SeasonListSerializer,
    SeasonSerializer,
)


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.prefetch_related("genres", "cast").select_related("country")
    serializer_class = CardSerializer
    permission_classes = [HasGroupPermission]
    permission_groups = {
        "create": ["moderator", "admin"],
        "list": ["_Public"],
        "retrieve": ["_Public"],
        "partial_update": ["moderator", "admin"],
        "destroy": ["admin"],
    }

    def get_serializer_class(self):
        if self.action == "list":
            return CardListSerializer
        elif self.action == "create":
            return CardCreateSerializer
        return CardSerializer


class SeasonViewSet(viewsets.ModelViewSet):
    queryset = Season.objects.select_related("card")
    serializer_class = SeasonSerializer
    permission_classes = [HasGroupPermission]
    permission_groups = {
        "create": ["moderator", "admin"],
        "list": ["_Public"],
        "retrieve": ["_Public"],
        "partial_update": ["moderator", "admin"],
        "destroy": ["moderator", "admin"],
    }

    def get_serializer_class(self):
        if self.action == "list":
            return SeasonListSerializer
        elif self.action == "create":
            return SeasonCreateSerializer
        return SeasonSerializer


class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.select_related("season")
    serializer_class = EpisodeSerializer
    permission_classes = [HasGroupPermission]
    permission_groups = {
        "create": ["admin", "moderator"],
        "list": ["_Public"],
        "retrieve": ["_Public"],
        "partial_update": ["moderator", "admin"],
        "destroy": ["admin", "moderator"],
    }

    def get_serializer_class(self):
        if self.action == "list":
            return EpisodeListSerializer
        elif self.action == "create":
            return EpisodeCreateSerializer
        return EpisodeSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("name",)


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("name",)


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.prefetch_related("person", "item")
    serializer_class = MembershipSerializer
