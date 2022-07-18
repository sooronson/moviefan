from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Movie


# Create your views here.

class MovieListView(ListView):
    template_name = 'movies/movie_list.html'
    model = Movie
    context_object_name = 'movie_list'


class MovieDetailView(DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'movies/movie.html'

