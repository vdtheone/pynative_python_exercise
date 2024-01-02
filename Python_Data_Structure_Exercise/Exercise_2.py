# Remove and add item in a list

# Write a program to remove the item present at index 4 and add it to the 2nd 
# position and at the end of the list.

list1 = [54, 44, 27, 79, 91, 41]
print(list1)    

item = list1.pop(4)
print(list1)
list1.insert(2,item)
print(list1)
list1.append(item)
print(list1)