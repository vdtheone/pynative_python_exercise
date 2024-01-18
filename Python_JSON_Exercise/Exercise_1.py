# Exercise 1: Convert the following dictionary into JSON format

import json


data = {"key1" : "value1", "key2" : "value2"}

data = json.dumps(data)

print(data)
print(type(data))