# Calculate the multiplication and sum of two numbers

# Given two integer numbers, return their product only if the product is equal to or 
# lower than 1000. Otherwise, return their sum.

number1 = int(input("Enter number = "))
number2 = int(input("Enter number = "))

def Calculate(number1,number2):
    product = number1 * number2
    if product<=1000:
        return product
    return number1 + number2


result = Calculate(number1, number2)
print("The Result is ", result)