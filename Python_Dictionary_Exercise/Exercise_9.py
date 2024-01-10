# Get the key of a minimum value from the following dictionary

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

print(min(sample_dict.items())[0])
print(min(sample_dict, key=sample_dict.get))


data = [(1, 5), (2, 3), (3, 7), (4, 1)]
min_tuple = min(data, key=lambda x: x[1])  # Finds the tuple with the smallest second element
print(min_tuple)  # Output will be: (4, 1)

