from factory import Faker, django
from movies.models import Movie


class MovieFactory(django.DjangoModelFactory):
    class Meta:
        model = Movie

    title = Faker("sentence", nb_words=4)
    genre = Faker(
        "pylist", nb_elements=3, variable_nb_elements=True, value_type=["str"]
    )

movie_catalog = MovieFactory.build(5)
print(movie_catalog)