from rest_framework import viewsets

from .models import Person
from .serializers import PersonCreateSerializer, PersonListSerializer, PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return PersonListSerializer
        elif self.action == "create":
            return PersonCreateSerializer
        return PersonSerializer
