from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from breed.models import Breed
from .managers import DogQuerySet


# Create your models here.


class Dog(models.Model):
    name = models.CharField(max_length=150)
    age = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=150)
    color = models.CharField(max_length=200)
    favorite_food = models.CharField(max_length=250)
    favorite_toy = models.CharField(max_length=250)

    objects = DogQuerySet.as_manager()
