# Write a program to create function func1() to accept a variable length of arguments 
# and print their value.

args = 5

def func1(*args):
    for i in args:
        print(args)


func1("vishal", "dhaval", "nimesh")
func1("vishal", "dhaval")
func1("vishal", "dhaval", "nimesh", 12)
func1(12,10,15,78)