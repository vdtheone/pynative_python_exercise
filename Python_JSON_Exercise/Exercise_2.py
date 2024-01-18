# Exercise 2: Access the value of key2 from the following JSON

import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""

sampleJson = json.loads(sampleJson)
print(sampleJson['key2'])