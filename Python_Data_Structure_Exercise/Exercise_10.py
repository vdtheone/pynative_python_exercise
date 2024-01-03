# Remove duplicates from a list and create a tuple and find the minimum and maximum number

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

print("unique list = ",list(set(sample_list)))

unique_item = tuple(set(sample_list))

print("Tuple = ",unique_item)

print("Min = ",min(unique_item))
print("Max = ",max(unique_item))