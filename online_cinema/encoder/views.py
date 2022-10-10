from django_filters import rest_framework as filters
from rest_framework import viewsets
from users.permissions import HasGroupPermission

from .models import Trailer, Video
from .serializers import (
    TrailerCreateSerializer,
    TrailerListSerializer,
    TrailerSerializer,
    VideoCreateSerializer,
    VideoListSerializer,
    VideoSerializer,
)


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [HasGroupPermission]
    permission_groups = {
        "create": ["moderator", "admin"],
        "list": ["moderator", "admin"],
        "retrieve": ["moderator", "admin"],
        "partial_update": ["moderator", "admin"],
        "destroy": ["moderator", "admin"],
    }
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("status", "created_by", "item", "resolution", "created_at")

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return VideoListSerializer
        elif self.action == "create":
            return VideoCreateSerializer
        return VideoSerializer


class TrailerViewSet(viewsets.ModelViewSet):
    queryset = Trailer.objects.all()
    serializer_class = TrailerSerializer
    permission_classes = [HasGroupPermission]
    permission_groups = {
        "create": ["moderator", "admin"],
        "list": ["moderator", "admin"],
        "retrieve": ["moderator", "admin"],
        "partial_update": ["moderator", "admin"],
        "destroy": ["admin"],
    }
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("card", "resolution")

    def get_serializer_class(self):
        if self.action == "list":
            return TrailerListSerializer
        elif self.action == "create":
            return TrailerCreateSerializer
        return TrailerSerializer
