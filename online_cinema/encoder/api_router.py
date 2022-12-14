from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"videos", views.VideoViewSet)
router.register(r"tasks", views.ConvertTaskViewSet, basename="task")
