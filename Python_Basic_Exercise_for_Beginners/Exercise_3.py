# Write a program to accept a string from the user 
# and display characters that are present at an even index number.

str = "pynative"
output = "pntv"

for i in list(str[0::2]):
    print(i)

print("")

for i in str:
    if str.index(i) % 2 == 0:
        print(i)

print("")

for i in range(0, len(str)-1, 2):
    print(str[i])