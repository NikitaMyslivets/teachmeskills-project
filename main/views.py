from django.shortcuts import render
from .models import *
from .forms import *


def index(request):
    allMovies = Movie.objects.all()

    context = {
        'movie': allMovies
    }
    return render(request, 'main/index.html', context)
