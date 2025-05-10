from rest_framework import serializers

from breed.models import Breed


class BreedSerializer(serializers.ModelSerializer):
    count_dogs = serializers.IntegerField(read_only=True)

    class Meta:
        model = Breed
        fields = "__all__"
