# Exercise 4: Sort JSON keys in and write them into a file

import json


sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

with open("Python_JSON_Exercise\\test.txt", "w") as file:
    json.dump(sampleJson, file, indent=2, sort_keys=True)

print("Done writing JSON data into a file")


