from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from online_cinema.users.permissions import HasGroupPermission

from .models import Card, Country, Episode, Genre, Membership, Season
from .serializers import (
    BasicCardSerializer,
    BasicEpisodeSerializer,
    CardCreateSerializer,
    CardListSerializer,
    CountrySerializer,
    EpisodeCreateSerializer,
    EpisodeListSerializer,
    FullCardSerializer,
    FullEpisodeSerializer,
    GenreSerializer,
    MembershipSerializer,
    SeasonCreateSerializer,
    SeasonListSerializer,
    SeasonSerializer,
)


class CardViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Card.objects.prefetch_related("genres", "cast").select_related("country")
    permission_classes = [HasGroupPermission]
    permission_groups = {
        "create": ["moderator", "admin"],
        "list": ["_Public"],
        "retrieve": ["_Public"],
        "partial_update": ["moderator", "admin"],
        "destroy": ["admin"],
    }
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("type", "released_year", "country", "genres", "is_available")

    def get_queryset(self):
        queryset = super().get_queryset()
        user_group = list(self.request.user.groups.values_list("name", flat=True))
        cast = self.kwargs.get("parent_lookup_membership")
        genres = self.kwargs.get("parent_lookup_genres")
        country = self.kwargs.get("parent_lookup_country")

        if ("viewer" in user_group) or (not user_group):
            queryset = queryset.filter(is_available=True)
        else:
            queryset = queryset

        if cast:
            return queryset.filter(cast=cast)
        elif genres:
            return queryset.filter(genres=genres)
        elif country:
            return queryset.filter(country=country)
        else:
            return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return CardListSerializer
        if self.request.user.is_staff or (
            "moderator" == self.request.user.groups.values_list("name", flat=True)[0]
        ):
            if self.action == "create":
                return CardCreateSerializer
            else:
                return FullCardSerializer
        return BasicCardSerializer


class SeasonViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
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
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("card",)

    def get_serializer_class(self):
        if self.action == "list":
            return SeasonListSerializer
        elif self.action == "create":
            return SeasonCreateSerializer
        return SeasonSerializer


class EpisodeViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Episode.objects.select_related("season")
    serializer_class = FullEpisodeSerializer
    permission_classes = [HasGroupPermission]
    permission_groups = {
        "create": ["admin", "moderator"],
        "list": ["_Public"],
        "retrieve": ["_Public"],
        "partial_update": ["moderator", "admin"],
        "destroy": ["admin", "moderator"],
    }
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("viewers", "season", "updated_to")

    def get_serializer_class(self):
        if self.action == "list":
            return EpisodeListSerializer
        if self.request.user.is_staff or (
            "moderator" in list(self.request.user.groups.values_list("name", flat=True))
        ):
            if self.action == "create":
                return EpisodeCreateSerializer
            else:
                return FullEpisodeSerializer
        return BasicEpisodeSerializer


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
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("person", "item", "character")
