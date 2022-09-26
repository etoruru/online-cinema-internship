from django.urls import include, path

from .api_router import router

urlpatterns = [path("", include((router.urls, "comments")))]
