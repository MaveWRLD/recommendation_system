import pytest

from movies.models import Movie
from movies.serializers import MovieSerializer


@pytest.mark.django_db
def test_movie_serialzer():
    valid_data = {"title": "Inception", "genres": ["Action", "Sci-fi"]}

    serializer = MovieSerializer(data=valid_data)

    assert serializer.is_valid()
    movie = serializer.save()

    assert Movie.objects.count() == 1

    movie_created = Movie.objects.get()
    movie_created.title == valid_data["title"]
    movie_created.genres == valid_data["genres"]


@pytest.mark.django_db
def test_movie_invalid_data():
    invalid_data = {"genres": ["Action", "Sci-fi"]}

    serializer = MovieSerializer(data=invalid_data)

    assert not serializer.is_valid()

    assert "title" in serializer.errors


@pytest.mark.django_db
def test_serialize_movie_instance():
    movie = Movie.objects.create(
        title="Inception", genres=["Action", "Sci.fi"]
    )

    serializer = MovieSerializer(movie)

    assert serializer.data == {
        "id": movie.id,
        "title": movie.title,
        "genres": movie.genres,
    }
