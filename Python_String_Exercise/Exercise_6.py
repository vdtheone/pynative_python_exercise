# Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"

letters = 0
digits = 0
special_symbols = 0

for i in str1:
    if i.isalpha():
        letters+=1
    elif i.isnumeric():
        digits+=1
    else:
        special_symbols+=1

print("letters = ",letters, "digits = ", digits, "special_symbols = ", special_symbols)