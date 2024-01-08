# Concatenate two lists index-wise

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result = []

for i in range(len(list1)):
    result.append(list1[i]+list2[i])

print(result)

list3 = [i + j for i, j in zip(list1, list2)]

print(list3)
