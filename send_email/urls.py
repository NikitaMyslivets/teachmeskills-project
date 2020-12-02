from django.contrib import admin
from django.urls import path, include
from .views import ContactView
from .apps import SendEmailConfig

app_name = SendEmailConfig.name

urlpatterns = [
    path('', ContactView.as_view(), name='contact')
]