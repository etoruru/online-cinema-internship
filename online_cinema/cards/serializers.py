from cards.models import Card, Country, Episode, Genre, Membership, Season
from rest_framework import serializers


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["id", "name"]


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ["character", "person"]


class CardSerializer(serializers.HyperlinkedModelSerializer):
    country = serializers.ReadOnlyField(source="country.name")
    cast = MembershipSerializer(source="cards", many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    # trailers = serializers.ReadOnlyField(source='trailer.id')

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
            # "trailers",
        ]


class CardListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ["url", "id", "name"]


class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    season = serializers.ReadOnlyField(source="season.id")
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
    card = serializers.ReadOnlyField(source="card.id")
    episodes = serializers.HyperlinkedRelatedField(
        many=True, view_name="episode-detail", read_only=True
    )

    class Meta:
        model = Season
        fields = ["url", "id", "name", "card", "episodes"]


class SeasonListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Season
        fields = ["url", "id", "name"]


class SeasonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ["name", "card"]


class EpisodeCreateSerializer(serializers.ModelSerializer):
    season = SeasonCreateSerializer()

    class Meta:
        model = Episode
        fields = [
            "num",
            "name",
            "preview",
            "description",
            "viewers",
            "updated_to",
            "season",
        ]

    def create(self, validated_data):

        season = Season.objects.get()
        validated_data["season"] = season

        episode = Episode.objects.create(**validated_data)
        return episode


class MembershipCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ["character", "person"]


class CardCreateSerializer(serializers.HyperlinkedModelSerializer):
    country = CountrySerializer()
    cast = MembershipCreateSerializer(many=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Card
        fields = [
            "name",
            "type",
            "description",
            "released_year",
            "country",
            "banner",
            "is_available",
            "genres",
            "cast",
        ]

    def create(self, validated_data):
        cast = validated_data.pop("cast", [])
        country_data = validated_data.pop("country")
        country = Country.objects.get(**country_data)
        genres = validated_data.pop("genres", [])
        card = Card.objects.create(**validated_data, country=country)

        card.genres.add(genres)
        for membership in cast:
            membership["item"] = card
            Membership.objects.create(**membership)
        return card
