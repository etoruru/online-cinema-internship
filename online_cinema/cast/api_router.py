from rest_framework_extensions.routers import ExtendedDefaultRouter

from online_cinema.cards.views import CardViewSet

from . import views

router = ExtendedDefaultRouter()
router.register(r"person", views.PersonViewSet).register(
    r"cards",
    CardViewSet,
    "persons-memberships-card",
    parents_query_lookups=["person__card", "membership"],
)
