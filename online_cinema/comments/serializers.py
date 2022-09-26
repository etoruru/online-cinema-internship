from comments.models import Bookmark, Comment, History, Subscription
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    episode = serializers.ReadOnlyField(source="episode.id")

    class Meta:
        model = Comment
        fields = ["id", "text", "created_at", "user", "episode"]


class CommentListSerializer(CommentSerializer):
    class Meta(CommentSerializer.Meta):
        fields = ["id"]


class CommentCreateSerializer(CommentSerializer):
    user = serializers.CharField(write_only=True, source="user.username")
    episode = serializers.IntegerField(write_only=True, source="episode.id")


class HistorySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    episode = serializers.ReadOnlyField(source="episode.id")

    class Meta:
        model = History
        fields = ["id", "date_visited", "user", "episode"]


class HistoryListSerializer(HistorySerializer):
    class Meta(HistorySerializer.Meta):
        fields = ["id"]


class HistoryCreateSerializer(HistorySerializer):
    user = serializers.CharField(write_only=True, source="user.username")
    episode = serializers.IntegerField(write_only=True, source="episode.id")


class BookmarkSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    card = serializers.ReadOnlyField(source="card.name")

    class Meta:
        model = Bookmark
        fields = ["id", "user", "card"]


class BookmarkListSerializer(BookmarkSerializer):
    class Meta(BookmarkSerializer.Meta):
        fields = ["id"]


class BookmarkCreateSerializer(BookmarkSerializer):
    user = serializers.CharField(write_only=True, source="user.username")
    card = serializers.IntegerField(write_only=True, source="card.id")


class SubSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Subscription
        fields = ["id", "expired_date", "user"]


class SubListSerializer(SubSerializer):
    class Meta(SubSerializer.Meta):
        fields = ["id"]


class SubCreateSerializer(SubSerializer):
    user = serializers.CharField(write_only=True, source="user.username")
