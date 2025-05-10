from rest_framework import viewsets

from .serializers import BreedSerializer
from .models import Breed
from .managers import BreedQuerySet


# Create your views here.
class BreedViewSet(viewsets.ModelViewSet):
    serializer_class = BreedSerializer
    http_method_names = ["get", "post", "put", "delete"]

    def get_queryset(self):
        queryset: BreedQuerySet = Breed.objects.all()

        if self.action == "list":
            return queryset.get_breed_list_w_count_dogs()

        return queryset
