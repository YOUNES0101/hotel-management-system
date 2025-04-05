from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_method
from django.contrib.auth import login as login_method
from django.contrib import messages


# Create your views here.
def home(request):
    # This is a simple view that returns a HTTP response

    return render(request, 'home.html')
    # Later you can return a rendered template instead

    # retiejfhzjufsi


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_method(request, user)
            messages.success(request, 'You are successfully logged in')

        else:
            return render(request, 'login.html', {'message': 'Invalid username or password!'})
    return render(request, 'login.html', {'message': ''})


def sign_up(request):

     return render(request, 'sign_up.html',{'message': ''})
