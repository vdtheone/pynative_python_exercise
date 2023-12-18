# Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]

l = len(list1)

for i in range(l-1,-1,-1):
    print(list1[i])


print("")

reversed_list = reversed(list1)

for i in reversed_list:
    print(i)