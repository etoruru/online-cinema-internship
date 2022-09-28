from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from users.permissions import HasGroupPermission

from .models import Person
from .serializers import PersonCreateSerializer, PersonListSerializer, PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [HasGroupPermission]
    permission_groups = {
        "create": ["admin"],
        "list": ["_Public"],
        "retrieve": ["_Public"],
        "partial_update": ["_Public"],
        "delete": ["_Public"],
    }

    def get_serializer_class(self):
        if self.action == "list":
            return PersonListSerializer
        elif self.action == "create":
            return PersonCreateSerializer
        return PersonSerializer
