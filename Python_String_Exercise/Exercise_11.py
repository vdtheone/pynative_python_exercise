# Write a program to count occurrences of all characters within a string

str1 = "Apple"

data = {}

for i in str1:
    data[i] = str1.count(i)


print(data)
