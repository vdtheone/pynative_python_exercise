# Write a program to count the total number of digits in a number using a while loop.

num = 45665
# print(len(str(num)))

count = 0
while num!=0:
    num = num//10
    count+=1

print(count)