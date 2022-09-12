from cards.models import Card, Episode, Season
from rest_framework import serializers


class CardSerializer(serializers.HyperlinkedModelSerializer):
    country = serializers.ReadOnlyField(source="country.name")
    cast = serializers.HyperlinkedRelatedField(
        many=True, view_name="membership-detail", read_only=True
    )
    genres = serializers.HyperlinkedRelatedField(
        many=True, view_name="genre-detail", read_only=True
    )
    trailers = serializers.HyperlinkedRelatedField(
        many=True, view_name="trailer-detail", read_only=True
    )

    class Meta:
        model = Card
        fields = [
            "url",
            "id",
            "name",
            "description",
            "released_year",
            "country",
            "banner",
            "is_available",
            "genres",
            "cast",
            "trailers",
        ]


class CardListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ["url", "id", "name"]


class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    season = serializers.ReadOnlyField(source="season.name")
    comments = serializers.HyperlinkedRelatedField(
        many=True, view_name="comment-detail", read_only=True
    )
    videos = serializers.HyperlinkedRelatedField(
        many=True, view_name="video-detail", read_only=True
    )

    class Meta:
        model = Episode
        fields = [
            "url",
            "id",
            "num",
            "name",
            "preview",
            "description",
            "viewers",
            "updated_to",
            "season",
            "comments",
            "videos",
        ]


class EpisodeListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episode
        fields = ["url", "id", "num", "name"]


class SeasonSerializer(serializers.HyperlinkedModelSerializer):
    card = serializers.ReadOnlyField(source="card.name")
    episodes = serializers.HyperlinkedRelatedField(
        many=True, view_name="episodes-detail", read_only=True
    )

    class Meta:
        model = Season
        fields = ["url", "id", "name", "card", "episodes"]


class SeasonListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Season
        fileds = ["url", "id", "name"]
