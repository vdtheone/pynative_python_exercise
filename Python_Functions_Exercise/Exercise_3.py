# Write a program to create function calculation() 
# such that it can accept two variables and calculate addition 
# and subtraction. Also, it must return both addition and subtraction 
# in a single return call.


def calculation(num1, num2):
    sum = num1+num2
    sub = num1-num2
    return sum, sub

sum, sub = calculation(40,10)
res = calculation(40,10)

print(sum, sub)
print(res)