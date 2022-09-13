from cast.models import Person
from cast.serializers import PersonSerializer
from rest_framework import viewsets


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    # def perform_create(self, serializer):
    #     serializer.save(cards=)
