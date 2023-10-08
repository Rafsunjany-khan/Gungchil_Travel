from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Bus, Travel

def index(request):
    travel = Travel.objects.all()
    return render(request, 'index.html', {'travel': travel})
def bus(request):
    bus = Bus.objects.all()
    return render(request, 'buslist.html', {'bus': bus})

def viewSeat(request):
    return render(request, 'seat.html')
def book(request):
    return render(request, 'booking.html')

def payment(request):
    return render(request, 'payment.html')