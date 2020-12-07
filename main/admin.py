from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'url')
    list_display_links = ('name', )


@admin.register(Genre)
class GenreAdmin(TranslationAdmin):
    list_display =('name', 'url')


@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    list_display = ('name', 'release_date', )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user')
