from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"card", views.CardViewSet)
router.register(r"season", views.SeasonViewSet)
router.register(r"episode", views.EpisodeViewSet)

urlpatterns = [path("", include(router.urls))]
