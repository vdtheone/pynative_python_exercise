# Write a program to display all prime numbers within a range

# range
start = 25
end = 50


for i in range(start, end+1):
    if i > 1:   
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            print(i)
