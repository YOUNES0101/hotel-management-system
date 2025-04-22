from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from hotel_app.models import CustomUser




# def home_view(request):
#     signup_form = CustomUserCreationForm(data=request.POST or None)  # Create or bind the form
#     login_form = AuthenticationForm(data=request.POST or None)  # Create or bind the login form
#     if request.method == "POST" and signup_form.is_valid():
#         signup_form.save()  # Save the user if the form is valid
#         messages.success(request, "Your account has been created successfully!")
#         return redirect('home')  # Redirect to the home page

#     context = {
#         'signup_form': signup_form,  # Pass the form to the template
#     }
#     #authentication form to check if the user is already registered or not

#     return render(request, 'hotel_app/home.html', context)


def home_view(request):
    signup_form = CustomUserCreationForm()
    login_form = AuthenticationForm()

    if request.method == "POST":
        # Handle Signup
        if 'signup' in request.POST:
            signup_form = CustomUserCreationForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save(commit=False)
                user.save()
                login(request, user)  # log the new user in
                messages.success(request, "Account created and logged in!")
                return redirect('home')
            else:
                messages.error(request, "Signup failed. Please correct the errors.")

        # Handle Login
        elif 'login' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('home')
            else:
                messages.error(request, "Login failed. Please check your credentials.")

    context = {
        'signup_form': signup_form,
        'login_form': login_form,
    }
    return render(request, 'hotel_app/home.html', context)

