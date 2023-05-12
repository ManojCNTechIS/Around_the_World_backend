from django.shortcuts import render
from .serializers import Placesserializers
from rest_framework import generics, filters
from .models import Places
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class PlacesList(generics.ListAPIView):
    queryset = Places.objects.order_by('-created_at').all()
    serializer_class = Placesserializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_field = ['Category']
    search_field = ['name', 'description']
