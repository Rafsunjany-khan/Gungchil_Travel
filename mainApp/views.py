from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import *
import random
import string
def index(request):
    travel = Travel.objects.all()
    return render(request, 'index.html', {'travel': travel})
def bus(request):
    bus = Bus.objects.all()
    return render(request, 'buslist.html', {'bus': bus})

def viewSeat(request):
    seat = Seat.objects.all()

    if request.method == 'POST':
        pnr1 = request.POST.get('pnr')
        bus = request.POST.get('busno')
        tdate = request.POST.get('tdate')
        departure = request.POST.get('depar')
        destination = request.POST.get('dest')
        time = request.POST.get('time')
        price = request.POST.get('price')
        print("The pnr is:", pnr1)
        context={
            'seat': seat,
            'pnr': pnr1,
            'bus': bus,
            'date': tdate,
            'departure': departure,
            'destination': destination,
            'time': time,
            'price': price,
        }
    return render(request, 'seat.html',context)

def book(request):
    issued = Issued.objects.all()

    if request.method == "POST":
        pnr = request.POST.get('pnr')
        seat = request.POST.get('seat')
        issue = request.POST.get('issue')
        name = request.POST.get('fullName')
        email = request.POST.get('email')
        contact_no = request.POST.get('contactNo')
        address = request.POST.get('address')
        tdate = request.POST.get('tdate')
        departure = request.POST.get('depar')
        destination = request.POST.get('dest')
        busno = request.POST.get('busno')
        time = request.POST.get('time')
        price = request.POST.get('price')
        print("The pnr no 2 is: ",pnr)
        #sn = Booked(pnrNo=trv, issuedBy=issue, name=name, email=email, contactNo=contact_no, address=address)

    context ={
        'pnr': pnr,
        'issued': issued,
        'seat': seat,
        'bus': busno,
        'tdate': tdate,
        'departure': departure,
        'destination': destination,
        'time': time,
        'price': price,
    }
    return render(request, 'booking.html', context)
def test1(request):
    if request.method == "POST":
        pnr = request.POST.get('pnr')
        seat = request.POST.get('seat')
        tdate = request.POST.get('tdate')
        departure = request.POST.get('depar')
        destination = request.POST.get('dest')
        busno = request.POST.get('busno')
        price = request.POST.get('price')
        time = request.POST.get('time')
        issue = request.POST.get('issue')
        name = request.POST.get('fullName')
        email = request.POST.get('email')
        contact_no = request.POST.get('contactNo')
        address = request.POST.get('address')
        print("The 3rd pnr is: ", pnr)
        book = Booked(pnrNo=pnr,busNo=busno,issuedBy=issue,timeSchedule=time,travelDate=tdate,departure=departure,destination=destination,name=name,email=email,contactNo=contact_no,address=address,seatNo=seat,price=price,total_price=price)
        book.save()

        context ={
            'pnr': pnr,
            'seat': seat,
            'date': tdate,
            'departure': departure,
            'destination': destination,
            'busno': busno,
            'price': price,
            'time': time,
            'issue': issue,
            'name': name,
            'email': email,
            'contact': contact_no,
        }

    return render(request, 'test1.html',context)
def payment(request):
    return render(request, 'payment.html')

def travel(request):
    seat = Seat.objects.all()
    travel = Travel.objects.all()
    if request.method == 'POST':
        pnr_n = request.POST.get('pnr')
        print("The Pnr is : ", pnr_n)
    return render(request, 'travel.html', {'travel': travel, 'seat': seat})
def search(request):
    date1 = request.GET.get('d', '')
    query = request.GET.get('p', '')
    query1 = request.GET.get('q', '')
    if query or query1 or date1:
        results = Travel.objects.filter(travelDate__icontains=date1, departure__name__icontains=query, destination__name__icontains=query1)
        print('the name: ',results)
    else:
        results= Travel.objects.all()

    return render(request, 'search.html', {'results': results, 'date':date1, 'query': query, 'query1': query1})
def ticket(request):

    tick = Booked.objects.all()[0:6]
    return render(request, 'ticket.html', {'ticket': tick})

