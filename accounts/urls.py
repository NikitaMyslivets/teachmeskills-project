from django.urls import path, include
from . import views
from .apps import AccountsConfig

app_name = AccountsConfig.name

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]