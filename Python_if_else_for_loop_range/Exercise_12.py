# Display Fibonacci series up to 10 terms

def Fibonacci(terms):
    first = 0
    second = 1
    for i in range(terms):
        print(first, end=" ")
        temp = first + second
        first = second
        second = temp


Fibonacci(10)