# Find words with both alphabets and numbers

str1 = "Emma25 is Data scientist50 and AI Expert"

temp = str1.split()

res = []

for i in temp:
     if any(char.isalpha() for char in i) and any(char.isdigit() for char in i):
        res.append(i)


for i in res:
    print(i)