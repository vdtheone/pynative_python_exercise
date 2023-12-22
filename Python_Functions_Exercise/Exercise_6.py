# Write a program to create a recursive function 
# to calculate the sum of numbers from 0 to 10.

def recursive_func(num):
    if num==1:
        return 1
    else:
        return num + recursive_func(num-1) 

print("Sum = ", recursive_func(10))