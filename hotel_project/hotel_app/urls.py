from django.urls import path
from . import views

urlpatterns = [
    # Define your URL patterns here
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.sign_up, name='signup'),

]