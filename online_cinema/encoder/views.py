from rest_framework import viewsets

from .models import Trailer, Video
from .serializers import (
    TrailerListSerializer,
    TrailerSerializer,
    VideoListSerializer,
    VideoSerializer,
)


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, item=self.request.data["episode"])

    def get_serializer_class(self):
        if self.action == "list":
            return VideoListSerializer
        return VideoSerializer


class TrailerViewSet(viewsets.ModelViewSet):
    queryset = Trailer.objects.all()
    serializer_class = TrailerSerializer

    def perform_create(self, serializer):
        serializer.save(
            card=self.request.data["card"], video=self.request.data["video"]
        )

    def get_serializer_class(self):
        if self.action == "list":
            return TrailerListSerializer
        return TrailerSerializer
