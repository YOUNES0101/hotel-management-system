from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import room, CustomUser, reservation
from .forms import UserLoginForm, UserRegistrationForm
import json
from datetime import datetime, timedelta

def home(request):
    # Get featured rooms or any other data you want to display
    try:
        rooms = room.objects.all()[:4]  # Get first 4 rooms for featured section
    except:
        # Handle case where room model might have been renamed
        rooms = []
    return render(request, 'hotel_app/home.html', {'rooms': rooms})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Since we're using CustomUser with email as USERNAME_FIELD
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been successfully logged in.")
                return redirect('home')
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = UserLoginForm()

    return redirect('home')

def user_signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Create new user
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])

            # Set first_name and last_name from the full name
            if 'name' in form.cleaned_data and form.cleaned_data['name']:
                name_parts = form.cleaned_data['name'].split(' ', 1)
                user.first_name = name_parts[0]
                if len(name_parts) > 1:
                    user.last_name = name_parts[1]

            user.save()

            # Log the user in
            login(request, authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password']))
            messages.success(request, "Account successfully created. Welcome to HORIZONH!")
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegistrationForm()

    return redirect('home')

def rooms(request):
    rooms = room.objects.all()
    return render(request, 'hotel_app/rooms.html', {'rooms': rooms})

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

@login_required
@csrf_exempt
def create_reservation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            room_id = data.get('room_id')
            check_in_date = datetime.strptime(data.get('check_in_date'), '%Y-%m-%d').date()
            check_out_date = datetime.strptime(data.get('check_out_date'), '%Y-%m-%d').date()

            # Validation: check_in_date < check_out_date
            if check_in_date >= check_out_date:
                return JsonResponse({'success': False, 'error': 'La date de départ doit être après la date d\'arrivée.'})

            # Vérifier si la chambre existe
            try:
                room_obj = room.objects.get(id=room_id)
            except room.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Chambre non trouvée'})

            # Vérifier si la chambre est disponible pour ces dates
            if reservation.objects.filter(
                room=room_obj,
                check_out_date__gt=check_in_date,
                check_in_date__lt=check_out_date
            ).exists() or reservation.objects.filter(
                room=room_obj,
                check_out_date=check_in_date
            ).exists():
                return JsonResponse({
                    'success': False,
                    'error': "La chambre n'est pas disponible pour ces dates (conflit avec une réservation existante)"
                })

            # Double check: ne pas créer si une réservation identique existe déjà
            if reservation.objects.filter(
                client=request.user,
                room=room_obj,
                check_in_date=check_in_date,
                check_out_date=check_out_date
            ).exists():
                return JsonResponse({
                    'success': False,
                    'error': "Vous avez déjà une réservation identique pour cette chambre et ces dates."
                })

            # Créer la réservation UNIQUEMENT si aucune réservation existante
            new_reservation = reservation.objects.create(
                client=request.user,
                room=room_obj,
                check_in_date=check_in_date,
                check_out_date=check_out_date
            )

            # Mettre à jour la disponibilité de la chambre (optionnel)
            room_obj.is_available = False
            room_obj.save()

            return JsonResponse({
                'success': True,
                'message': 'Réservation créée avec succès',
                'reservation_id': new_reservation.id
            })
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Données JSON invalides'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Méthode non autorisée'})

def get_available_dates(request, room_id):
    # Get all reservations for this room
    existing_reservations = reservation.objects.filter(room_id=room_id)
    
    # Create a set of all dates for the next 90 days
    today = datetime.now().date()
    all_dates = set([(today + timedelta(days=x)).isoformat() 
                     for x in range(90)])
    
    # Remove booked dates
    for booking in existing_reservations:
        current_date = booking.check_in_date
        while current_date <= booking.check_out_date:
            all_dates.discard(current_date.isoformat())
            current_date += timedelta(days=1)
    
    return JsonResponse({'available_dates': list(all_dates)})

