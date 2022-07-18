from django.contrib import admin

from .models import (
    Category, MovieShots, Movie, Actor,
    RatingStar, Rating, Genre, Comment
)


# Register your models here.

@admin.register(Category, Movie, Genre)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name']


admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Comment)


