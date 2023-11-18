from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Bus, Travel, Booked
import random
import string
def index(request):
    travel = Travel.objects.all()
    return render(request, 'index.html', {'travel': travel})
def bus(request):
    bus = Bus.objects.all()
    return render(request, 'buslist.html', {'bus': bus})

def viewSeat(request):
    if request.method == 'POST':
        seat = request.POST.get('seat')
        return seat


    return render(request, 'seat.html')
def book(request):

    return render(request, 'booking.html')

def payment(request):
    return render(request, 'payment.html')

def test(request):
    seat= viewSeat(request)
    pnrBus = Travel.objects.values_list('pnrNo')
    print("The pnr is: ", pnrBus)
    if request.method == 'POST':
        issuedBy = request.POST.get('issuedBy')
        issueFrom = request.POST.get('issueFrom')
        name = request.POST.get('fullName')
        email = request.POST.get('email')
        contact = request.POST.get('contactNo')
        address = request.POST.get('address')
        print("Issued bY: ",seat, issuedBy)
        print("Issued from: ",issueFrom,name,email,contact,address)

        context = {
            'pnrBus': pnrBus,
            'seat': seat,
        }
    return render(request, 'test.html', context)

def ticket(request):
    tick = Booked.objects.all()[0:4]
    return render(request, 'ticket.html', {'ticket': tick})
