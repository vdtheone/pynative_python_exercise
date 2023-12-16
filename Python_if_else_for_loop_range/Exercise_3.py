# Calculate the sum of all numbers from 1 to a given number

num = int(input("enter number = "))

sum = 0
while num>=1:
    sum = sum + num
    num-=1

print(sum)