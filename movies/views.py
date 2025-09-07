from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status, views
from rest_framework.response import Response

from .models import Movie
from .serializers import MovieSerializer

class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# Create your views here.
