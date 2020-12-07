from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'actor', 'director', )