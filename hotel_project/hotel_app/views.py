from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View


def home_view(request):
    return render(request, 'hotel_app/home.html')
