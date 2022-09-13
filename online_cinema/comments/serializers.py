from comments.models import Bookmark, Comment, History, Subscription
from rest_framework import serializers


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    episode = serializers.ReadOnlyField(source="episode.id")

    class Meta:
        model = Comment
        fields = ["url", "id", "text", "created_at", "user", "episode"]


class HistorySerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    episode = serializers.ReadOnlyField(source="episode.id")

    class Meta:
        model = History
        fields = ["url", "id", "date_visited", "user", "episode"]


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    card = serializers.ReadOnlyField(source="card.name")

    class Meta:
        model = Bookmark
        fields = ["url", "id", "user", "card"]


class SubSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Subscription
        fields = ["url", "id", "expired_date", "user"]
