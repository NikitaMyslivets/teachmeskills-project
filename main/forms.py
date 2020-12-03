from django import forms

from .models import *


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'description', 'actor', 'director', 'genre', 'release_date', 'average_rating',
                  'time', 'image', 'video', 'category')


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('comment', 'rating')
