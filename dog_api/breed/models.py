from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .managers import BreedQuerySet

# Create your models here.


class Breed(models.Model):
    class SizeChoices(models.TextChoices):
        TINY = "Tiny"
        SMALL = "Small"
        MEDIUM = "Medium"
        LARGE = "Large"

    name = models.CharField(max_length=128)
    size = models.CharField(choices=SizeChoices.choices, max_length=6)
    friendliness = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    shedding_amount = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    exercise_needs = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    objects = BreedQuerySet.as_manager()
