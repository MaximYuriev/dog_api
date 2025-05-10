from typing import Self
from django.db import models
from django.db.models import Count


class BreedQuerySet(models.QuerySet):
    def get_breed_list_w_count_dogs(self) -> Self:
        return self.annotate(count_dogs=Count("dog"))
