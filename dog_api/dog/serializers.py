from rest_framework import serializers

from dog.models import Dog


class DogSerializer(serializers.ModelSerializer):
    breed_avg_age = serializers.FloatField(read_only=True)
    dog_same_breed_count = serializers.IntegerField(read_only=True, source="count_dog")

    class Meta:
        model = Dog
        fields = "__all__"
