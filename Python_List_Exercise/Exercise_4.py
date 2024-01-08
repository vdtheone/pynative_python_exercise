# Concatenate two lists in the following order

# output = ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

output = [i + j for i in list1 for j in list2]

print(output)

for i in list1:
    for j in list2:
        print(i+j)