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
        fields = ["character", "person", "item"]


class MembershipCardSerializer(MembershipSerializer):
    class Meta(MembershipSerializer.Meta):
        fields = ["character", "person"]


class MembershipPersonSerializer(MembershipSerializer):
    class Meta(MembershipSerializer.Meta):
        exclude = ["person"]
        fields = ["character", "item"]


class CardSerializer(serializers.HyperlinkedModelSerializer):
    country = serializers.ReadOnlyField(source="country.name")
    cast = MembershipCardSerializer(source="membership", many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    # trailers = serializers.ReadOnlyField(source='trailer.id')

    class Meta:
        model = Card
        fields = [
            "url",
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
    country = CountrySerializer()
    cast = MembershipCardSerializer(many=True, source="character")
    genres = GenreSerializer(many=True)

    def create(self, validated_data):
        cast = validated_data.pop("cast", [])
        country_data = validated_data.pop("country")
        country = Country.objects.get(**country_data)
        genres = validated_data.pop("genres", [])
        card = Card.objects.create(**validated_data, country=country)
        for genre in genres:
            card.genres.add(genre["id"])

        for membership in cast:
            person = Person.objects.filter(id=membership["person"])
            membership["item"] = card
            membership["person"] = person
            Membership.objects.create(**membership)

        # if card.type == "F":
        #     season = Season.objects.create(name="1", card=card)
        #     episode = Episode.objects.create(season=season)

        return card


class SeasonSerializer(serializers.HyperlinkedModelSerializer):
    card = serializers.ReadOnlyField(source="card.id")
    episodes = serializers.HyperlinkedRelatedField(
        many=True, view_name="episode-detail", read_only=True
    )

    class Meta:
        model = Season
        fields = ["url", "id", "name", "card", "episodes"]


class SeasonListSerializer(SeasonSerializer):
    class Meta(SeasonSerializer.Meta):
        fields = ["url", "id", "name"]


class SeasonCreateSerializer(SeasonSerializer):
    class Meta(SeasonSerializer.Meta):
        fields = ["name", "card"]


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


class EpisodeListSerializer(EpisodeSerializer):
    class Meta(EpisodeSerializer.Meta):
        model = Episode
        fields = ["url", "id"]


class EpisodeCreateSerializer(EpisodeSerializer):
    season = SeasonCreateSerializer()

    def create(self, validated_data):

        season = Season.objects.get()
        validated_data["season"] = season

        episode = Episode.objects.create(**validated_data)
        return episode
