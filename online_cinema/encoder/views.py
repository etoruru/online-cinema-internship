from rest_framework import viewsets

from .models import Trailer, Video
from .serializers import TrailerSerializer, VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user, item=self.request.data["episode_id"]
        )


class TrailerViewSet(viewsets.ModelViewSet):
    queryset = Trailer.objects.all()
    serializer_class = TrailerSerializer

    def perform_create(self, serializer):
        serializer.save(
            card=self.request.data["card_id"], video=self.request.data["video_id"]
        )
