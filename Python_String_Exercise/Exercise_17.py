# Removal all characters from a string except integers

str1 = 'I am 25 years and 10 months old'

data = ''
for i in str1:
    if i.isdigit():
        data += ''.join(i)

print(data)