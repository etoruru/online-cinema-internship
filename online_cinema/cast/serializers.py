from cast.models import Person
from rest_framework import serializers


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    cards = serializers.HyperlinkedRelatedField(
        many=True, view_name="card.name", read_only=True
    )

    class Meta:
        model = Person
        fields = ["url", "id", "firstname", "lastname", "picture", "cards"]
