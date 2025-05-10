from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import BreedViewSet


router = DefaultRouter()

router.register(r"", BreedViewSet, basename="")

urlpatterns = [path("", include(router.urls))]
