# Exercise 6: Convert the following Vehicle Object into JSON

import json
from json import JSONEncoder

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

vehicleJson  = json.dumps(vehicle, indent=2, cls=VehicleEncoder)

print(vehicleJson)

data = { "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }