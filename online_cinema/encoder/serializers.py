from rest_framework import serializers

from online_cinema.encoder.file_uploader import file_upload
from online_cinema.encoder.tasks import convert_video_to_hls

from .models import ConvertTask, Video


class VideoSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")
    item = serializers.ReadOnlyField(source="item.id")

    class Meta:
        model = Video
        fields = [
            "id",
            "source_file_path",
            "created_at",
            "status",
            "file_format",
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
        file_upload.apply_async(args=[video.source_file_path])
        return video

    class Meta(VideoSerializer.Meta):
        fields = [
            "source_file_path",
            "file_format",
            "item",
        ]


class ConvertTaskSerializer(serializers.ModelSerializer):
    video = serializers.ReadOnlyField(source="video.id")

    class Meta:
        model = ConvertTask
        fields = ["id", "output", "video"]


class ConvertTaskCreateSerializer(ConvertTaskSerializer):
    video = None

    def create(self, validated_data):
        task = ConvertTask.objects.create(**validated_data)
        video = validated_data.get("video")
        if video.file_format.lower() == "hls":
            convert_video_to_hls.apply_async(
                args=[video.pk, task.pk, video.source_file_path], queue="video"
            )
        return task

    class Meta(ConvertTaskSerializer.Meta):
        fields = ["video"]
