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
                username = login_form.cleaned_data.get('username')  # This will be the email in your case
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, f"Welcome back!")
                    return redirect('home')
                else:
                    messages.error(request, "Invalid email or password.")
            else:
                messages.error(request, "Invalid email or password.")

    context = {
        'signup_form': signup_form,
        'login_form': login_form,
    }
    return render(request, 'hotel_app/home.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, "You have been successfully logged out!")
    return redirect('home')

