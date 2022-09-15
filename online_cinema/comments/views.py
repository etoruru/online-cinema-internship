from rest_framework import viewsets

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
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, episode_id=self.request.data["episode"])

    def get_serializer_class(self):
        if self.action == "list":
            return CommentListSerializer
        elif self.action == "create":
            return CommentCreateSerializer
        return CommentSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, episode_id=self.request.data["episode"])

    def get_serializer_class(self):
        if self.action == "list":
            return HistoryListSerializer
        elif self.action == "create":
            return HistoryCreateSerializer
        return HistorySerializer


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, card_id=self.request.data["card"])

    def get_serializer_class(self):
        if self.action == "list":
            return BookmarkListSerializer
        elif self.action == "create":
            return BookmarkCreateSerializer
        return BookmarkSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return SubListSerializer
        elif self.action == "create":
            return SubCreateSerializer
        return SubSerializer
