# Write a program to check if the given number is a palindrome number.

num = int(input("enter number = "))


def check_pallindrom(num):
    num = str(num)
    if num[:] == num[::-1]:
        print("pallindrom")
    else:
        print("Not pallindrom")


check_pallindrom(num)


def check_pallindrom_number(num):
    temp = num

    reverse_num = 0
    while temp != 0:
        rem = temp % 10
        temp = temp // 10
        reverse_num = (reverse_num * 10) + rem

    if num == reverse_num:
        print("yes")
    else:
        print("no")


check_pallindrom_number(num)
