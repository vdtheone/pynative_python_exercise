# Delete a list of keys from a dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for i in keys:
    # del sample_dict[i]  #This will also work
    sample_dict.pop(i)

print(sample_dict)

sample_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}
print(sample_dict)
