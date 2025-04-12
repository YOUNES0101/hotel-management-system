from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import CustomUserCreationForm

from django.contrib import messages



# def home_view(request):
#     return render(request, 'hotel_app/home.html')


def home_view(request):
    # Render the home page with both login and signup modals if you like.
    # For now, we focus on the signup part.
    signup_form = CustomUserCreationForm(data=request.POST or None) if request.method == "POST" else CustomUserCreationForm()
    context = {
        'signup_form': signup_form,
    }
    return render(request, 'hotel_app/home.html', context)





def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully!")
            return redirect('home')  # Redirect to home or another page
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'hotel_app/home.html', {'signup_form': form})