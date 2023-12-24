# Write a program to create a new string made of the middle three 
# characters of an input string.

name = input("Enter name - ")

mi = int(len(name)/2)

print(name[mi-1:mi+2])