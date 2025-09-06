from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "genre"]


# Register your models here.
