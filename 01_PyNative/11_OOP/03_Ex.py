#Create a Vehicle class without any variables and methods
# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class


class Vehicle:
    def __init__(self):
        pass

class Bus(Vehicle):
    def __init__(self):
        super().__init__(self)
