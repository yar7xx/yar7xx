from django.shortcuts import render
from .models import Flight

def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flights.html', {'flights': flights})