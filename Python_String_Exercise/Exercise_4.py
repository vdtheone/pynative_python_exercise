# Create a new string made of the first, middle, and last characters of each input string

# Given two strings, s1 and s2, write a program to return a new string made of 
# s1 and s2’s first, middle, and last characters.

s1 = "America"
s2 = "Japan"

s1_mid = len(s1)//2
s2_mid = len(s2)//2

first = s1[:1] + s2[:1]
middle = s1[s1_mid] + s2[s2_mid]
last = s1[-1:] + s2[-1:]
print(first+middle+last)