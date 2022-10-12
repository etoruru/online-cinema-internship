from rest_framework_extensions.routers import ExtendedDefaultRouter

from online_cinema.cards.views import EpisodeViewSet

from . import views

router = ExtendedDefaultRouter()
router.register(r"comments", views.CommentViewSet, basename="comment")
router.register(r"history", views.HistoryViewSet, basename="history").register(
    r"episodes", EpisodeViewSet, "historys-episode", parents_query_lookups=["history"]
)
router.register(r"bookmarks", views.BookmarkViewSet, basename="bookmark")
router.register(r"subscriptions", views.SubscriptionViewSet, basename="subscription")
