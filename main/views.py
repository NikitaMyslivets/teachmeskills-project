from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Avg
from django.core.paginator import Paginator


def index(request):
    query = request.GET.get('title')
    allMovies = None
    allGenres = Genre.get_all_genres()

    if query:
        allMovies = Movie.objects.filter(name__icontains=query)
    else:
        genreID = request.GET.get('genre')
        if genreID:
            allMovies = Movie.get_all_movies_by_genreid(genreID).order_by('-id')
        else:
            allMovies = Movie.get_all_movies().order_by('-id')

        '''pagination'''

    paginator = Paginator(allMovies, 3)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''

    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''

        '''end pagination'''


    context = {
        'genres': allGenres,
        'movies': page,
        'next_page_url': next_url,
        'prev_page_url': prev_url,
    }

    return render(request, 'main/home.html', context)


def detail(request, id):
    movie = Movie.objects.get(id=id)
    reviews = Review.objects.filter(movie=id).order_by('-comment')

    average = reviews.aggregate(Avg('rating'))['rating__avg']
    if average == None:
        average = 0
    average = round(average, 2)

    context = {
        'movie': movie,
        'reviews': reviews,
        'average': average,
    }

    return render(request, 'main/detail.html', context)


def add_review(request, id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=id)
        if request.method == 'POST':
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST['comment']
                data.rating = request.POST['rating']
                data.user = request.user
                data.movie = movie
                data.save()
                return redirect('main:detail', id)
        else:
            form = ReviewForm()
        return render(request, 'main/detail.html', {'form': form})
    else:
        return redirect('accounts:login')



