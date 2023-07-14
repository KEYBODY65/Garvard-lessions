from django.shortcuts import render
from .models import Flight, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    all = Flight.objects.all()
    return render(request, 'flights/indes.html', {
        'flights': all  # выводим значения из бд
    })


def current_flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, 'flights/current_flight.html', {
        'flight': flight,
        'passengers': flight.passenger.all(),  # related_name - passenger, вот для чего используется(пример)
        'non_passengers': Passenger.objects.exclude(flights=flight).all() # exclude - используется для получения набора объектов, которых нет во flights, в отличии от filter: который искал бы тех, кто соответсвует
    })


def book(request, flight_id):
    if request.method == 'POST':
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST['passenger']))  # <select name="passenger">
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('current_flight', args=(flight_id,)))  # сделал так,чтобы нас перенаправило обратно на path('<int:flight_id>', current_flight, name='flights'),
