from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"cards", views.CardViewSet)
router.register(r"seasons", views.SeasonViewSet)
router.register(r"episodes", views.EpisodeViewSet)
router.register(r"genres", views.GenreViewSet)
router.register(r"countries", views.CountryViewSet)
router.register(r"membership", views.MembershipViewSet)

urlpatterns = [path("", include(router.urls))]
