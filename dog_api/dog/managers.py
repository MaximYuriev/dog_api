from typing import Self

from django.db import models
from django.db.models import Avg, Count, OuterRef, Subquery


class DogQuerySet(models.QuerySet):
    def get_dog_list_w_breed_average_age(self) -> Self:
        sub = self.filter(breed=OuterRef("breed")).values("breed").annotate(avg_age=Avg("age")).values("avg_age")
        query = self.annotate(breed_avg_age=Subquery(sub))
        return query

    def get_dog_w_count_dog_same_breed(self) -> Self:
        sub = self.filter(breed=OuterRef("breed")).values("breed").annotate(count_dog=Count("id")).values("count_dog")
        query = self.annotate(count_dog=Subquery(sub))
        return query
