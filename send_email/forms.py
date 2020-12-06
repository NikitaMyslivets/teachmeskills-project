from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control mb-4',
                'placeholder': 'Name',
                'id': 'defaultSubscriptionFormPassword',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control mb-4',
                'placeholder': 'E-mail',
                'id': 'defaultSubscriptionFormEmail',
            })
        }
        labels = {
            'name': '',
            'email': ''
        }