from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_extensions.mixins import NestedViewSetMixin

from online_cinema.users.permissions import HasGroupPermission, IsOwnerOrReadOnly

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


class CommentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.select_related("user", "episode")
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("user", "episode")

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get("parent_lookup_episode"):
            return queryset.filter(episode=self.kwargs["parent_lookup_episode"])
        else:
            return queryset

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
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("user", "episode")

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(user=user)

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
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("user", "card")

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(user=user)

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
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = "expired_date"

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return SubListSerializer
        elif self.action == "create":
            return SubCreateSerializer
        return SubSerializer
