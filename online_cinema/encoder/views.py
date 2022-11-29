from django_filters import rest_framework as filters
from rest_framework import viewsets

from online_cinema.users.permissions import HasGroupPermission

from .models import ConvertTask, Video
from .serializers import (
    ConvertTaskCreateSerializer,
    ConvertTaskSerializer,
    VideoCreateSerializer,
    VideoListSerializer,
    VideoSerializer,
)


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.select_related("item")
    permission_classes = [HasGroupPermission]
    permission_groups = {
        "create": ["moderator", "admin"],
        "list": ["viewer", "moderator", "admin"],
        "retrieve": ["viewer", "moderator", "admin"],
        "partial_update": ["moderator", "admin"],
        "destroy": ["moderator", "admin"],
    }
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("status", "created_by", "item", "file_format", "created_at")

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return VideoListSerializer
        elif self.action == "create":
            return VideoCreateSerializer
        return VideoSerializer


class ConvertTaskViewSet(viewsets.ModelViewSet):
    queryset = ConvertTask.objects.select_related("video")
    permission_classes = [HasGroupPermission]
    permission_groups = {
        "create": ["moderator", "admin"],
        "list": ["viewer", "moderator", "admin"],
        "retrieve": ["viewer", "moderator", "admin"],
        "partial_update": ["moderator", "admin"],
        "destroy": ["moderator", "admin"],
    }
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("video", "created_by")

    def get_serializer_class(self):
        if self.action == "create":
            return ConvertTaskCreateSerializer
        return ConvertTaskSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
