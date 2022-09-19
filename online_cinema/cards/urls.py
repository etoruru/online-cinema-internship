from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"cards", views.CardViewSet)
router.register(r"seasons", views.SeasonViewSet)
router.register(r"episodes", views.EpisodeViewSet)

urlpatterns = [path("", include(router.urls))]
