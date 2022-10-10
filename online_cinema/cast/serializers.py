from cast.models import Person
from rest_framework import serializers


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
