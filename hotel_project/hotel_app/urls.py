from django.urls import path
from . import views
from dashboard_app import views as dashboard_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', dashboard_views.DashboardHomeView.as_view(), name='dashboard_home'),
]

