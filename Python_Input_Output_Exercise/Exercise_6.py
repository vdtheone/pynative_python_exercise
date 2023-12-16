# Write all content of a given file into a new file by skipping line number 5

with open("E:\\Internship\\Python_Practice\\pynative_python_exercise\\Python_Input_Output_Exercise\\test.txt", 'r')as f:
    z = f.readlines()


with open("E:\\Internship\\Python_Practice\\pynative_python_exercise\\Python_Input_Output_Exercise\\test1.txt", 'w')as f:
    count = 0
    for line in z:
        if count==4:
            count+=1
            continue
        else:
            f.write(line)
            count+=1
        