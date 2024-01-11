# Add a list of elements to a set

# Given a Python list, Write a program to add all its elements into a given set.

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

# for i in sample_list:
#     sample_set.add(i)

# print(sample_set)

sample_set.update(sample_list)

print(sample_set)