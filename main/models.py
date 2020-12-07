from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import utc
from embed_video.fields import EmbedVideoField
from django.utils import timezone

class Category(models.Model):
    name = models.CharField('Категория', max_length=50)
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    name = models.CharField('Жанр', max_length=50)
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_genres():
        return Genre.objects.all()

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=4000)
    actor = models.CharField(max_length=300)
    director = models.CharField(max_length=300)
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    release_date = models.PositiveSmallIntegerField(default=0)
    average_rating = models.FloatField(default=0)
    time = models.CharField(max_length=50)
    image = models.URLField(default=None, null=True)
    video = models.URLField(default=None, null=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


    @staticmethod
    def get_all_movies():
        return Movie.objects.all()

    @staticmethod
    def get_all_movies_by_genreid(genre_id):
        if genre_id:
            return Movie.objects.filter(genre=genre_id)
        else:
            return Movie.get_all_genres()

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-id']

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=2000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


