# Exercise 4: Class Inheritance

# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() 
# a default value of 50.


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


obj = Bus("scholl bus", 180, 18)

print(obj.seating_capacity())