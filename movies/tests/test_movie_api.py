import json

import pytest
from django.test import override_settings
from django.urls import reverse
from rest_framework import status

from movies.models import Movie

from .factories import MovieFactory


@pytest.mark.django_db
def test_create_movie(client):
    # arrange
    url = reverse("movies:movie-api")
    data = {"title": "A New Hope", "genres": json.dumps(["Sci-fi", "Adventure"])}

    # act
    response = client.post(url, json=data)

    # assert
    assert response.status_code == status.HTTP_201_CREATED, response.json()
    assert Movie.objects.filter(title="A New Hope").count() == 1


@pytest.mark.django_db
def test_retrieve_movie(client):
    movie = MovieFactory()
    url = reverse("movies:movie-api-detail", kwargs={"pk": movie.id})

    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": movie.id,
        "title": movie.title,
        "genres": movie.genres,
    }


@pytest.mark.django_db
def test_update_movie(client):
    movie = MovieFactory
    new_title = ""
    url = reverse("movies:movie-api-detail", kwargs={"pk": movie.id})
    data = {"title": new_title}

    response = client.put(url, data=data, content_type="application/json")

    assert response.status_code == status.HTTP_200_OK, response.json()
    movie = Movie.objects.filter(id=movie.id).first()
    assert movie
    assert movie.title == new_title


@pytest.mark.django_db
def test_delete_movie(client):
    movie = MovieFactory()
    url = reverse("movies:movie-api-detail", kwargs={"pk": movie.id})

    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Movie.objects.filter(id=movie.id).exists()


@pytest.mark.django_db
@override_settings(REST_FRAMEWORK={"PAGE_SIZE": 10})
def test_list_movie_pagination(client):
    movies = MovieFactory.create_batch(10)
    url = reverse("movies:movie-api-list")

    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert "count" in data
    assert "next" in data
    assert "previous" in data
    assert "results" in data

    assert data["count"] == 10
    assert data["next"] is not None

    assert len(data["results"]) == 10

    returned_movie_ids = {movie["id"] for movie in data["results"]}
    expected_movie_ids = {movie.id for movie in movies}
    assert returned_movie_ids == expected_movie_ids

    for movie_data in data["results"]:
        assert set(movie_data.keys()) == {"id", "title", "genres"}
