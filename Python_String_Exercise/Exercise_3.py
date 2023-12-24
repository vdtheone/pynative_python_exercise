# Given two strings, s1 and s2. Write a program to create a new string s3 by 
# appending s2 in the middle of s1.

s1 = "Ault"
s2 = "Kelly"

mid = int(len(s1)/2)
x = s1[:mid:]
x = x + s2
x = x + s1[mid:]

print(x)