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

    # person = serializers.PrimaryKeyRelatedField(read_only=True)
    # item = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Membership
        fields = ["id", "character", "person"]


# class MembershipCreateSerializer(MembershipSerializer):
#
#     class Meta:
#         model = Membership
#         fields = ["character", "person"]


class CardSerializer(serializers.ModelSerializer):
    cast = MembershipSerializer(source="card_to_person", many=True, read_only=True)
    country = serializers.StringRelatedField()
    genres = serializers.StringRelatedField(many=True)

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
        ]


class CardListSerializer(CardSerializer):
    class Meta(CardSerializer.Meta):
        fields = ["id", "name"]


class CardCreateSerializer(CardSerializer):
    country = None
    cast = MembershipSerializer(many=True, source="card_to_person")
    genres = None

    def create(self, validated_data):
        people = validated_data.pop("card_to_person")
        genres = validated_data.pop("genres")
        card = Card.objects.create(**validated_data)
        card.genres.set(genres)

        characters = []
        for membership in people:
            character = Membership(
                person=membership["person"],
                item=card,
                character=membership["character"],
            )
            characters.append(character)
        Membership.objects.bulk_create(characters)
        return card

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
        ]


class SeasonSerializer(serializers.ModelSerializer):
    card = serializers.PrimaryKeyRelatedField(read_only=True)
    episodes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Season
        fields = ["id", "name", "card", "episodes"]


class SeasonListSerializer(SeasonSerializer):
    class Meta(SeasonSerializer.Meta):
        fields = ["id", "name"]


class SeasonCreateSerializer(SeasonSerializer):
    card = None

    class Meta(SeasonSerializer.Meta):
        fields = ["name", "card"]


class EpisodeSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    videos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Episode
        fields = [
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
        fields = ["id"]


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
