
from django.shortcuts import render
from django.contrib.auth.models import User
from hotel_app.models import reservation, room ,CustomUser  # Assuming these models exist

def dashboard_home(request):
    return render(request, 'dashboard_app/home.html')

def manage_users(request):
    users = CustomUser.objects.all()
    return render(request, 'dashboard_app/manage_users.html', {'users': users})

def manage_reservations(request):
    reservations = reservation.objects.all()
    return render(request, 'dashboard_app/manage_reservations.html', {'reservations': reservations})

def manage_rooms(request):
    rooms = room.objects.all()
    return render(request, 'dashboard_app/manage_rooms.html', {'rooms': rooms})