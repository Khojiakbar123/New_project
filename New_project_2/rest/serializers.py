from rest_framework import serializers
from rest.models import CarRest


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarRest
        fields = ("title", "model", "manufactured", "color", "max_speed", "horsepower")
