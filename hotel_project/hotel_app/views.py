from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # This is a simple view that returns a HTTP response
    # Later you can return a rendered template instead
    return HttpResponse("Welcome to Hotel Management System!")
    # retiejfhzjufsi


