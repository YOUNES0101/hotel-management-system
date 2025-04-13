from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import CustomUserCreationForm
from django.contrib import messages




def home_view(request):
    signup_form = CustomUserCreationForm(data=request.POST or None)  # Create or bind the form

    if request.method == "POST" and signup_form.is_valid():
        signup_form.save()  # Save the user if the form is valid
        messages.success(request, "Your account has been created successfully!")
        return redirect('home')  # Redirect to the home page

    context = {
        'signup_form': signup_form,  # Pass the form to the template
    }
    return render(request, 'hotel_app/home.html', context)


