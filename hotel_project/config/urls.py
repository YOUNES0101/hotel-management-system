from django.contrib import admin
from django.urls import path, include
from hotel_app import views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', views.home, name="home"),
     path('login/', views.login, name="login"),
     path('singup/', views.sign_up, name="singup"),

]