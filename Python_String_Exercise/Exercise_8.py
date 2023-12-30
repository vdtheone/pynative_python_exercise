# String characters balance Test

# Write a program to check if two strings are balanced. For example, strings s1 and s2
# are balanced if all the characters in the s1 are present in s2. The character’s position
# doesn’t matter.

s1 = "Yn"
s2 = "PYnative"


print(s1 in s2)

s1 = "Ynf"
s2 = "PYnative"

print(s1 in s2)


def string_balance_test(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag


s1 = "Yn"
s2 = "PYnative"
flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)