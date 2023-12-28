# Create a mixed String using the following rules

# Given two strings, s1 and s2. Write a program to create a new string s3 
# made of the first char of s1, then the last char of s2, 
# Next, the second char of s1 and second last char of s2, 
# and so on. Any leftover chars go at the end of the result.

s1 = "Abc"
s2 = "Xyz"

result = s1[0]+s2[len(s2)-1]+s1[1]+s2[len(s2)-2]+s1[len(s1)-1]+s2[0]

print(result)


s1 = "Abc"
s2 = "Xyz"

# get string length
s1_length = len(s1)
s2_length = len(s2)

# get length of a bigger string
length = s1_length if s1_length > s2_length else s2_length
result = ""

# reverse s2
s2 = s2[::-1]

# iterate string 
# s1 ascending and s2 descending
for i in range(length):
    if i < s1_length:
        result = result + s1[i]
    if i < s2_length:
        result = result + s2[i]

print(result)