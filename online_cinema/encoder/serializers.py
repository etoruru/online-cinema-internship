from rest_framework import serializers

from online_cinema.encoder.tasks import convert_video

from .models import Trailer, Video


class VideoSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")
    item = serializers.ReadOnlyField(source="item.id")

    class Meta:
        model = Video
        fields = [
            "id",
            "filename",
            "filepath",
            "created_at",
            "status",
            "resolution",
            "created_by",
            "item",
        ]


class VideoListSerializer(VideoSerializer):
    class Meta(VideoSerializer.Meta):
        fields = ["id"]


class VideoCreateSerializer(VideoSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")
    item = None

    def create(self, validated_data):
        video = Video.objects.create(**validated_data)
        convert_video.apply_async(
            args=[video.filename, video.filepath],
        )
        return video

    class Meta(VideoSerializer.Meta):
        fields = [
            "filename",
            "resolution",
            "item",
        ]


class TrailerSerializer(serializers.ModelSerializer):
    card = serializers.ReadOnlyField(source="trailers")
    video = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Trailer
        fields = ["id", "card", "video"]


class TrailerListSerializer(VideoSerializer):
    class Meta(VideoSerializer.Meta):
        fields = ["id"]


class TrailerCreateSerializer(VideoSerializer):
    card = None
    video = None

    class Meta(VideoSerializer.Meta):
        fields = ["card", "video"]
