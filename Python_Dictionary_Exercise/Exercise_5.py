# Create a dictionary by extracting the keys from a given dictionary

# Write a Python program to create a new dictionary by extracting the mentioned 
# keys from the below dictionary.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

res = {}

for i in sample_dict:
    if i in keys:
        res[i] = sample_dict[i]

print(res)

new_dict = {k:sample_dict[k] for k in keys}

print(new_dict)
