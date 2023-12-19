# Reverse a given integer number

num = 76542

reverse_num = 0
while num !=0:
    rem = num % 10
    reverse_num = (reverse_num * 10) + rem
    print(reverse_num)
    num = num // 10

print(reverse_num)


