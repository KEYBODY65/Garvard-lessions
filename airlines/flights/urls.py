from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('<int:flight_id>', current_flight, name='flights'),
    path('<int:flight_idt>/book', book, name='book')
]
