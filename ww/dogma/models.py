from django.db import models

class Airline(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Airport(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=3, unique=True)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} – {self.city}"


class Flight(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    flight_number = models.CharField(max_length=10)
    departure_airport = models.ForeignKey(Airport, related_name='departures', on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey(Airport, related_name='arrivals', on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    economy_price = models.DecimalField(max_digits=8, decimal_places=2)
    business_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.airline.code}{self.flight_number}"


class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    passport_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Booking(models.Model):
    PASSENGER_CLASS = [('economy', 'Эконом'), ('business', 'Бизнес')]

    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_class = models.CharField(max_length=10, choices=PASSENGER_CLASS)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Бронь: {self.passenger} – {self.flight}"