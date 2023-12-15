# Write a program to remove characters from 
# a string starting from zero up to n and return a new string.

output = "tive"

def remove_chars(str, len):
    return str[len:]


print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))
print(remove_chars("pynative", 5))