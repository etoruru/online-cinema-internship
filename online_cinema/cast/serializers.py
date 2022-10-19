from rest_framework import serializers

from online_cinema.cast.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "firstname", "lastname", "picture"]


class PersonListSerializer(PersonSerializer):
    class Meta(PersonSerializer.Meta):
        fields = ["id"]


class PersonCreateSerializer(PersonSerializer):
    class Meta(PersonSerializer.Meta):
        fields = ["firstname", "lastname", "picture"]
