#    *  
#   * *  
#  * * *
# * * * *
#  * * *
#   * *
#    *


row = 4
space = row-1
for i in range(0, row):
    for j in range(0, space):
        print(end=" ")
    space = space - 1
    for j in range(0,i+1):
        print("*", end=" ")
    print(" ")

space = 1
for i in range(row-1,0,-1):
    for j in range(0, space):
        print(end=" ")
    space = space + 1
    for j in range(0,i):
        print("*", end=" ")
    print(" ")