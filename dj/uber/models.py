from datetime import datetime
from typing import List, Sequence, Optional

from django.db import models
from djantic import ModelSchema


from pydantic import BaseModel, PositiveInt, condecimal, AnyHttpUrl

# class Delivery(BaseModel):
#     name: str
#     type: str
#     vehicle_type = str
#     time_requested: datetime
#     date_requested: datetime
#     pounts_earned = int
#     tip_included = bool

# class Payment:
#     customer_price: int
#     customer_tip: int
#     to_uber: int 
#     fare: int
#     total: int

# class Earnings(BaseModel):
#     fare: int
#     promo: int
#     tip: int

class Customer(models.Model):
    name = models.CharField(max_length=200)
    payment = models.DecimalField(decimal_places=2, max_digits=6)
    tip = models.DecimalField(decimal_places=2, max_digits=6)
    
    trips = models.ForeignKey("Trip", on_delete=models.CASCADE)

# class Address(BaseModel):
#     street: str
#     lat: float
#     lng: float
#     customer: Customer
    

# class Trip(models.Model):
#     route = models.URLField()
#     duration = models.DateTimeField()
#     time_requested = models.DateTimeField()
    
    
        
#     pickup_location = models.CharField(max_length=50, blank=True)
#     pickup_address = models.CharField(max_length=255)
#     destination = models.CharField(max_length=255)
    
#     upfront_fare = models.DecimalField(max_digits=8, decimal_places=2)
#     mileage = models.DecimalField(max_digits=5, decimal_places=1)

# class Restaurant(models.Model):
#     name = models.CharField(max_length=155)
#     location = models.CharField(max_length=50, blank=True)

# class Delivery(models.Model):
#     trip_uuid = models.CharField(max_length=200, blank=True)
    
#     # service_type = models.TextChoices(Enum(trip_types))
#     request_time = models.CharField(max_length=200, blank=True)
#     pickup_address = models.CharField(max_length=200, blank=True)
    
#     trip_drop_time = models.CharField(max_length=200, blank=True)
#     drop_address = models.CharField(max_length=200, blank=True)
    
#     trip_distance = models.CharField(max_length=200, blank=True)
#     trip_status = models.CharField(max_length=200, blank=True)

# class Driver(models.Model):
#     UUID = models.CharField(max_length=200, blank=True)
#     first_name = models.CharField(max_length=200, blank=True)
#     last_name = models.CharField(max_length=200, blank=True)
    
# class Vehicle(models.Model):
#     name = models.CharField(max_length=255)
#     license_plate = models.CharField(max_length=200, blank=True)