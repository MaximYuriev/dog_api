from rest_framework import viewsets

from .managers import DogQuerySet
from .models import Dog
from .serializers import DogSerializer

# Create your views here.


class DogViewSet(viewsets.ModelViewSet):
    serializer_class = DogSerializer
    http_method_names = ["get", "post", "put", "delete"]

    def get_queryset(self):
        queryset: DogQuerySet = Dog.objects.select_related("breed")

        if self.action == "list":
            return queryset.get_dog_list_w_breed_average_age()

        if self.action == "retrieve":
            return queryset.get_dog_w_count_dog_same_breed()

        return queryset
