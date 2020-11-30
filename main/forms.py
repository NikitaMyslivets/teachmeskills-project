from django import forms
from .models import *


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'description', 'actor', 'director', 'genre', 'release_date', 'average_rating',
                  'time', 'image', 'video', 'category')