# Read line number 4 from the following file

with open(r'E:\Internship\Python_Practice\pynative_python_exercise\Python_Input_Output_Exercise\test.txt','r') as fp:
    count = 0
    lines = fp.readlines()
    print(lines[3])