from rest_framework import viewsets
from users.permissions import HasGroupPermission

from .models import Bookmark, Comment, History, Subscription
from .serializers import (
    BookmarkCreateSerializer,
    BookmarkListSerializer,
    BookmarkSerializer,
    CommentCreateSerializer,
    CommentListSerializer,
    CommentSerializer,
    HistoryCreateSerializer,
    HistoryListSerializer,
    HistorySerializer,
    SubCreateSerializer,
    SubListSerializer,
    SubSerializer,
)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related("user", "episode")
    serializer_class = CommentSerializer
    permission_classes = [HasGroupPermission]
    permission_groups = {
        "create": ["_Public"],
        "list": ["_Public"],
        "retrieve": ["_Public"],
        "partial_update": ["_Public"],
        "delete": ["_Public"],
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, episode_id=self.request.data["episode"])

    def get_serializer_class(self):
        if self.action == "list":
            return CommentListSerializer
        elif self.action == "create":
            return CommentCreateSerializer
        return CommentSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.select_related("user", "episode")
    serializer_class = HistorySerializer
    permission_classes = [HasGroupPermission]
    permission_groups = {
        "create": ["_Public"],
        "list": ["_Public"],
        "retrieve": ["_Public"],
        "delete": ["_Public"],
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, episode_id=self.request.data["episode"])

    def get_serializer_class(self):
        if self.action == "list":
            return HistoryListSerializer
        elif self.action == "create":
            return HistoryCreateSerializer
        return HistorySerializer


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.select_related("user", "card")
    serializer_class = BookmarkSerializer
    permission_classes = [HasGroupPermission]
    permission_groups = {
        "create": ["_Public"],
        "list": ["_Public"],
        "retrieve": ["_Public"],
        "delete": ["_Public"],
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, card_id=self.request.data["card"])

    def get_serializer_class(self):
        if self.action == "list":
            return BookmarkListSerializer
        elif self.action == "create":
            return BookmarkCreateSerializer
        return BookmarkSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.select_related("user")
    serializer_class = SubSerializer
    permission_classes = [HasGroupPermission]
    permission_groups = {
        "create": ["_Public"],
        "list": ["admin", "moderator"],
        "retrieve": ["_Public"],
        "partial_update": ["admin"],
        "delete": ["admin"],
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return SubListSerializer
        elif self.action == "create":
            return SubCreateSerializer
        return SubSerializer
