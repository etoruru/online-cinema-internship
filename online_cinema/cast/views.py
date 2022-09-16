from rest_framework import permissions, viewsets

from .models import Person
from .serializers import PersonCreateSerializer, PersonListSerializer, PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == "list":
            return PersonListSerializer
        elif self.action == "create":
            return PersonCreateSerializer
        return PersonSerializer
