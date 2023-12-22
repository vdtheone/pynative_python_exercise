# Generate a Python list of all the even numbers between 4 to 30

l = []
for i in range(4, 31):
    if i % 2 == 0:
        l.append(i)

print(l)


data = [i for i in range(4,31) if i%2==0]
print(data)