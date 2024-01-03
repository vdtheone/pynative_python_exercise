# Iterate a given list and check if a given element exists as a key’s value in a dictionary. 
# If not, delete it from the list

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

sample_list = []
for i in roll_number:
    if not i in sample_dict.values():
        sample_list.append(i)

print(sample_list)

sample_list = [item for item in roll_number if item in sample_dict.values()]

print(sample_list)