from rest_framework import serializers

from .models import Trailer, Video


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")
    item = serializers.ReadOnlyField(source="item.id")

    class Meta:
        model = Video
        fields = [
            "url",
            "id",
            "filename",
            "filepath",
            "created_at",
            "status",
            "resolution",
            "created_by",
            "item",
        ]


class TrailerSerializer(serializers.HyperlinkedModelSerializer):
    card = serializers.ReadOnlyField(source="card.name")
    video = serializers.HyperlinkedRelatedField(
        many=True, view_name="video-detail", read_only=True
    )

    class Meta:
        model = Trailer
        fields = ["url", "id", "card", "video"]
