from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"comments", views.CommentViewSet, basename="comment")
router.register(r"history", views.HistoryViewSet)
router.register(r"bookmarks", views.BookmarkViewSet)
router.register(r"subscriptions", views.SubscriptionViewSet)
