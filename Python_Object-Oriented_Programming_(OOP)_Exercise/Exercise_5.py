# Exercise 5: Define a property that must have the same value for every class instance (object)

# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.



class Vehicle:

    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass


School_bus = Bus("school bus", 180, 18)
car_obj = Bus("Audi Q8", 280, 18)

print(School_bus.color, School_bus.name, School_bus.max_speed, School_bus.mileage)
print(car_obj.color, car_obj.name, car_obj.max_speed, car_obj.mileage)

