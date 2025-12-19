# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

VolVoX = Vehicle(310, 200000)

print(VolVoX.max_speed, VolVoX.mileage)