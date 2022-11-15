from rest_framework_extensions.routers import ExtendedDefaultRouter

from online_cinema.encoder.views import ConvertTaskViewSet

from . import views

router = ExtendedDefaultRouter()
router.register(r"cards", views.CardViewSet, basename="cards").register(
    r"episodes",
    views.EpisodeViewSet,
    "cards-seasons-episode",
    parents_query_lookups=["card__episode", "season"],
)
router.register(r"seasons", views.SeasonViewSet)
router.register(r"genres", views.GenreViewSet).register(
    "cards", views.CardViewSet, "genre_cards", parents_query_lookups=["genres"]
)
router.register(r"countries", views.CountryViewSet).register(
    "cards", views.CardViewSet, "countries_cards", parents_query_lookups=["country"]
)
router.register(r"membership", views.MembershipViewSet)
router.register(r"episodes", views.EpisodeViewSet).register(
    r"videos", ConvertTaskViewSet, "cards-video", parents_query_lookups=["video"]
)
