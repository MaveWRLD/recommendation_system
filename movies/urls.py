from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = "movies"

router = DefaultRouter()

urlpatterns = [
    path("movies/", views.MovieListCreateAPIView.as_view(), name="movie-api"),
    path("movies/", views.MovieListCreateAPIView.as_view(), name="movie-api-list"),
    path("movies/<int:pk>", views.MovieDetailAPIView.as_view(), name="movie-api-detail"),
]
