from django.shortcuts import render
from rest_framework import generics
from .serializer import CarDetailSerializer, CarListSerializer
from .models import Car


# Create your views here.
class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarsListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
