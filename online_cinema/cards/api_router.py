from rest_framework_extensions.routers import ExtendedDefaultRouter

from online_cinema.comments.views import CommentViewSet

from . import views

router = ExtendedDefaultRouter()
router.register(r"cards", views.CardViewSet, basename="cards").register(
    r"episodes",
    views.EpisodeViewSet,
    "cards-seasons-episode",
    parents_query_lookups=["card__episode", "season"],
)
router.register(r"seasons", views.SeasonViewSet)
router.register(r"episodes", views.EpisodeViewSet).register(
    r"comments", CommentViewSet, "cards-comment", parents_query_lookups=["episode"]
)
router.register(r"genres", views.GenreViewSet).register(
    "cards", views.CardViewSet, "genre_cards", parents_query_lookups=["genres"]
)
router.register(r"countries", views.CountryViewSet).register(
    "cards", views.CardViewSet, "countries_cards", parents_query_lookups=["country"]
)
router.register(r"membership", views.MembershipViewSet)
