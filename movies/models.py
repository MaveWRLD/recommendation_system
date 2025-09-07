import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genres = models.JSONField(default=list)
    country = models.CharField(max_length=100, blank=True, null=True)
    extra_data = models.JSONField(default=dict)
    release_year = models.IntegerField(
        validators=[
            MinValueValidator(1888),
            MaxValueValidator(datetime.datetime.now().year),
        ],
        blank=True,
        null=True,
    )

    class Meta:
        unique_together = [("title", "country", "release_year")]

    def __str__(self):
        return f"{self.title}"


# Create your models here.
