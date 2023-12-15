# Write a function to return True if the first and last number of a given list is same. 
# If numbers are different then return False.

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def check_first_last_numbers(numbers):
    first_num = numbers[0]
    last_num = numbers[-1]
    if first_num==last_num:
        return True
    else:
        return False

print(check_first_last_numbers(numbers_x))
print(check_first_last_numbers(numbers_y))
