from django.urls import path
from . import views
from dashboard_app import views as dashboard_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('rooms/', views.rooms, name='rooms'),  # Added new URL pattern
    path('dashboard/', dashboard_views.DashboardHomeView.as_view(), name='dashboard_home'),
    path('create_reservation/', views.create_reservation, name='create_reservation'),
    path('get-available-dates/<int:room_id>/', views.get_available_dates, name='get-available-dates'),
]

