from cards.serializers import MembershipSerializer
from cast.models import Person
from rest_framework import serializers


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    cards = MembershipSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ["url", "id", "firstname", "lastname", "picture", "cards"]
