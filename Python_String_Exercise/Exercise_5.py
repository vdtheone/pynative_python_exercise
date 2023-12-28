# Arrange string characters such that lowercase letters should come first

# Given string contains a combination of the lower and upper case letters. 
# Write a program to arrange the characters of a string so that all lowercase 
# letters should come first.

str1 = "PyNaTive"

l = []

for i in str1:  
    l.append(ord(i))

l = sorted(l)
l.reverse()
s = ''
for i in l:
    s = s + chr(i)
print(s)


str1 = "PyNaTive"
print('Original String:', str1)
lower = []
upper = []
for char in str1:
    if char.islower():
        # add lowercase characters to lower list
        lower.append(char)
    else:
        # add uppercase characters to lower list
        upper.append(char)

# Join both list
sorted_str = ''.join(lower + upper)
print('Result:', sorted_str)