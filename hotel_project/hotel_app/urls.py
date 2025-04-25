from django.urls import path
from . import views
from dashboard_app import views as dashboard_views




urlpatterns = [
    path('', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', dashboard_views.DashboardHomeView.as_view(), name='dashboard_home'),

]

