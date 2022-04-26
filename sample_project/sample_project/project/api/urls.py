from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register("clients", views.ClientViewSet, basename="client")
router.register("projects", views.ProjectViewSet, basename="project")

urlpatterns = router.urls
