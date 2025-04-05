from django.urls import path
from . import views


urlpatterns = [
    # Define your URL patterns here
    path('login/', views.login, name='login'),


]