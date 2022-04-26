from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register("corevalues", views.CoreValueViewSet, basename="corevalue")

urlpatterns = router.urls
