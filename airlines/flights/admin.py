from django.contrib import admin
from .models import *


class FlightsAdmin(admin.ModelAdmin):
    """ для вывода в админ панель"""
    list_display = ('id', 'origin', 'destination', 'duration')


class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ('flights',)


admin.site.register(Airport)
admin.site.register(Flight, FlightsAdmin)
admin.site.register(Passenger, PassengerAdmin)
