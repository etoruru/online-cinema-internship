from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"videos", views.VideoViewSet)
router.register(r"trailers", views.TrailerViewSet)

urlpatterns = [path("", include(router.urls))]
