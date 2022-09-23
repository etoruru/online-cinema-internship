from cards.models import Card, Country, Episode, Genre, Membership, Season
from cast.models import Person
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
        fields = ["id", "character", "person", "item"]


class CardSerializer(serializers.ModelSerializer):
    cast = MembershipSerializer(source="character", many=True, read_only=True)

    # trailers = serializers.ReadOnlyField(source='trailer.id')

    def create(self, validated_data):
        pass

    class Meta:
        model = Card
        fields = [
            "id",
            "name",
            "type",
            "description",
            "released_year",
            "country",
            "banner",
            "is_available",
            "genres",
            "cast",
            # "trailers",
        ]


class CardListSerializer(CardSerializer):
    class Meta(CardSerializer.Meta):
        fields = ["url", "id", "name"]


class CardCreateSerializer(CardSerializer):
    country = None
    cast = None
    genres = None

    class Meta(CardSerializer.Meta):

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
            # "trailers",
        ]

    def create(self, validated_data):
        super().create(validated_data)

        cast = validated_data.pop("cast", [])
        genres = validated_data.pop("genres", [])
        country = Country.objects.get(pk=validated_data["country"])
        validated_data["country"] = country
        card = Card.objects.create(**validated_data)
        for genre in genres:
            card.genres.add(genre)

        characters = []
        for membership in cast:
            person = Person.objects.get(pk=membership["person"])
            character = Membership(
                person=person, item=card, character=membership["character"]
            )
            characters.append(character)
        Membership.objects.bulk_create(characters)
        return card


class SeasonSerializer(serializers.ModelSerializer):
    episodes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Season
        fields = ["id", "name", "card", "episodes"]


class SeasonListSerializer(SeasonSerializer):
    class Meta(SeasonSerializer.Meta):
        fields = ["id", "name"]


class SeasonCreateSerializer(SeasonSerializer):
    class Meta(SeasonSerializer.Meta):
        fields = ["name", "card"]


class EpisodeSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    videos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

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


class EpisodeListSerializer(EpisodeSerializer):
    class Meta(EpisodeSerializer.Meta):
        fields = ["url", "id"]


class EpisodeCreateSerializer(EpisodeSerializer):
    season = None

    class Meta(EpisodeSerializer.Meta):
        fields = [
            "num",
            "name",
            "preview",
            "description",
            "viewers",
            "updated_to",
            "season",
        ]
