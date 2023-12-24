#  Write a program to create a new string made of an input 
# string’s first, middle, and last character.


name = input("Enter name = ")

print(name[0],name[int(len(name)/2)],name[-1])