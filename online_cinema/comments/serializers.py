from comments.models import Bookmark, Comment, History, Subscription
from rest_framework import serializers


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    episode = serializers.ReadOnlyField(source="episode.id")

    class Meta:
        model = Comment
        fields = ["url", "id", "text", "created_at", "user", "episode"]


class CommentListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ["url", "id"]


class HistorySerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    episode = serializers.ReadOnlyField(source="episode.id")

    class Meta:
        model = History
        fields = ["url", "id", "date_visited", "user", "episode"]


class HistoryListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = History
        fields = ["url", "id"]


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    card = serializers.ReadOnlyField(source="card.name")

    class Meta:
        model = Bookmark
        fields = ["url", "id", "user", "card"]


class BookmarkListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookmark
        fields = ["url", "id"]


class SubSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Subscription
        fields = ["url", "id", "expired_date", "user"]


class SubListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscription
        fields = ["url", "id"]


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["text", "created_at", "user", "episode"]


class HistoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ["date_visited", "user", "episode"]


class BookmarkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ["user", "card"]


class SubCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["expired_date", "user"]
