from rest_framework import viewsets
from users.permissions import HasGroupPermission, IsOwnerOrReadOnly

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
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return CommentListSerializer
        elif self.action == "create":
            return CommentCreateSerializer
        return CommentSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.select_related("user", "episode")
    serializer_class = HistorySerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return HistoryListSerializer
        elif self.action == "create":
            return HistoryCreateSerializer
        return HistorySerializer


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.select_related("user", "card")
    serializer_class = BookmarkSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return BookmarkListSerializer
        elif self.action == "create":
            return BookmarkCreateSerializer
        return BookmarkSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.select_related("user")
    serializer_class = SubSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return SubListSerializer
        elif self.action == "create":
            return SubCreateSerializer
        return SubSerializer
