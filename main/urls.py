from django.urls import path, include
from . import views
from .apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', views.index, name='home'),
    path('details/<int:id>/', views.detail, name='detail'),
    path('addreview/<int:id>/', views.add_review, name='add_review'),

]