from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('users/', views.manage_users, name='manage_users'),
    path('reservations/', views.manage_reservations, name='manage_reservations'),
    path('rooms/', views.manage_rooms, name='manage_rooms'),
]
