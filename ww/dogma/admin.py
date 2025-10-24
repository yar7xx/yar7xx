from django.contrib import admin
from .models import Airline, Airport, Flight, Passenger, Booking


@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    ordering = ('name',)


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'city')
    search_fields = ('code', 'name', 'city')
    ordering = ('code',)


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = (
        'flight_number_display',
        'airline',
        'departure_airport',
        'arrival_airport',
        'departure_time',
        'arrival_time',
        'economy_price',
        'business_price'
    )
    list_filter = ('airline', 'departure_airport', 'arrival_airport')
    search_fields = ('flight_number', 'airline__name', 'airline__code')
    ordering = ('departure_time',)
    date_hierarchy = 'departure_time'

    def flight_number_display(self, obj):
        return str(obj)
    flight_number_display.short_description = 'Flight'
    flight_number_display.admin_order_field = 'flight_number'


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'passport_number')
    search_fields = ('first_name', 'last_name', 'passport_number')
    ordering = ('last_name', 'first_name')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'passenger',
        'flight_display',
        'seat_class',
        'total_price',
        'created_at'
    )
    list_filter = ('seat_class', 'created_at', 'flight__airline')
    search_fields = (
        'passenger__first_name',
        'passenger__last_name',
        'passenger__passport_number',
        'flight__flight_number',
        'flight__airline__name'
    )
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

    def flight_display(self, obj):
        return str(obj.flight)
    flight_display.short_description = 'Flight'
    flight_display.admin_order_field = 'flight__departure_time'