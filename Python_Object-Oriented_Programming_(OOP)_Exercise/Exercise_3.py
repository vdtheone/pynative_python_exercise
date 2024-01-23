# Exercise 3: Create a child class Bus that will inherit all of the variables 
# and methods of the Vehicle class

# Create a Bus object that will inherit all of the variables and methods of the parent 
# Vehicle class and display it.


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass
    

School_bus = Bus("school volvo", 180, 18)

print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)