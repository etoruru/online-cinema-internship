from cast.models import Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["url", "id", "firstname", "lastname", "picture", "character"]


class PersonListSerializer(PersonSerializer):
    class Meta(PersonSerializer.Meta):
        fields = ["url", "id"]


class PersonCreateSerializer(PersonSerializer):
    class Meta(PersonSerializer.Meta):
        fields = ["firstname", "lastname", "picture"]
