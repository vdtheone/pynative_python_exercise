# Calculate the sum and average of the digits present in a string

# Given a string s1, write a program to return the sum and average of the digits 
# that appear in the string, ignoring all other characters.


str1 = "PYnative29@#8496"

count, sum = 0, 0
for i in str1:
    if i.isdigit():
        count=count + 1
        sum=sum+int(i)

print("Sum is ", sum, "Average is ",sum/count)


