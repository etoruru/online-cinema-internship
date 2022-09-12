from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"comments", views.CommentViewSet)
router.register(r"history", views.HistoryViewSet)
router.register(r"bookmarks", views.BookmarkViewSet)
router.register(r"subscriptions", views.SubscriptionViewSet)

urlpatterns = [path("", include(router.urls))]
