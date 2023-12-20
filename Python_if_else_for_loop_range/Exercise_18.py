# Print the following pattern

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# x = 2
# for i in range(1,10):
#     if i>5:
#         # print("i = ",i)
#         i = i-x
#         # print("p = ",i)
#         for j in range(i):
#             print("*", end=" ")
#         x=x+2
#         # print("x = ",x)
#     else:
#         for j in range(i):
#             print("*", end=" ")

#     print(" ")



rows = 5

for i in range(0,rows):
    for j in range(0,i+1):
        print("*", end=" ")
    print("")

for i in range(rows,0,-1):
    for j in range(0, i-1):
        print("*", end=" ")
    print(" ")


