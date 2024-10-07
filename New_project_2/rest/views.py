from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest.models import CarRest
from rest.serializers import CarSerializer


# Create your views here.

class CarList(ListAPIView):
    queryset = CarRest.objects.all()
    serializer_class = CarSerializer
