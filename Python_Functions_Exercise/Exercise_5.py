# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate 
# the addition of a and b
# At last, an outer function will add 5 into addition and return it


def outer_function(a, b):
    def inner(a, b):
        return a+b
    result = inner(a, b)
    return result + 5

output = outer_function(10,20)
print(output)
