from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import DogViewSet


router = DefaultRouter()

router.register(r"", DogViewSet, basename="")

urlpatterns = [path("", include(router.urls))]
