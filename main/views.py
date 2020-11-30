from django.shortcuts import render
from .models import *
from .forms import *


def index(request):
    allMovies = Movie.objects.all()

    context = {
        'movies': allMovies
    }
    return render(request, 'main/home.html', context)


def detail(request, id):
    movie = Movie.objects.get(id=id)

    context = {
        'movie': movie
    }

    return render(request, 'main/detail.html', context)
