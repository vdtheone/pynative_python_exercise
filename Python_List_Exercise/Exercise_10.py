# Remove all occurrences of a specific item from a list.

# Given a Python list, write a program to remove all occurrences of item 20.

list1 = [5, 20, 15, 20, 25, 50, 20]

for i in list1:
    if i==20:
        list1.remove(20)

print(list1)    

print([i for i in list1 if i != 20])

list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5]