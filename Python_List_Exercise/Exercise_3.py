# Turn every item of a list into its square

numbers = [1, 2, 3, 4, 5, 6, 7]

squre = []

for i in numbers:
    squre.append(i**2)

print(squre)
print([i**2 for i in numbers])
