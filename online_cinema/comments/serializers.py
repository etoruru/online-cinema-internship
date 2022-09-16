from comments.models import Bookmark, Comment, History, Subscription
from rest_framework import serializers


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    episode = serializers.ReadOnlyField(source="episode.id")

    class Meta:
        model = Comment
        fields = ["url", "id", "text", "created_at", "user", "episode"]


class CommentListSerializer(CommentSerializer):
    class Meta(CommentSerializer.Meta):
        fields = ["url", "id"]


class CommentCreateSerializer(CommentSerializer):
    user = serializers.CharField(write_only=True, source="user.username")
    episode = serializers.IntegerField(write_only=True, source="episode.id")


class HistorySerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    episode = serializers.ReadOnlyField(source="episode.id")

    class Meta:
        model = History
        fields = ["url", "id", "date_visited", "user", "episode"]


class HistoryListSerializer(HistorySerializer):
    class Meta(HistorySerializer.Meta):
        fields = ["url", "id"]


class HistoryCreateSerializer(HistorySerializer):
    user = serializers.CharField(write_only=True, source="user.username")
    episode = serializers.IntegerField(write_only=True, source="episode.id")


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    card = serializers.ReadOnlyField(source="card.name")

    class Meta:
        model = Bookmark
        fields = ["url", "id", "user", "card"]


class BookmarkListSerializer(BookmarkSerializer):
    class Meta(BookmarkSerializer.Meta):
        fields = ["url", "id"]


class BookmarkCreateSerializer(BookmarkSerializer):
    user = serializers.CharField(write_only=True, source="user.username")
    card = serializers.IntegerField(write_only=True, source="card.id")


class SubSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Subscription
        fields = ["url", "id", "expired_date", "user"]


class SubListSerializer(SubSerializer):
    class Meta(SubSerializer.Meta):
        fields = ["url", "id"]


class SubCreateSerializer(SubSerializer):
    user = serializers.CharField(write_only=True, source="user.username")
