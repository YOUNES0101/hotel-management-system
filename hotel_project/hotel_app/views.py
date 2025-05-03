from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import room, CustomUser
from .forms import UserLoginForm, UserRegistrationForm

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

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

