import os
from datetime import datetime

fp = open(
    r"E:\Internship\Python_Practice\pynative_python_exercise\Python_Input_Output_Exercise\test.txt",
    "r",
)

print(fp.read())

fp.close()

# fp = open('sales.txt', 'x')
# fp.close()
fp = open("E:\Internship\Python_Practice\pynative_python_exercise\Python_Input_Output_Exercise\sales1.txt", "w")
fp.write("vishal prajapati")
fp.close()

print(os.listdir())

print(os.path.isfile("sales.txt"))


path = r"E:\Internship\Python_Practice\pynative_python_exercise\Python_Input_Output_Exercise"
file_name = "sales.txt"

with open(os.path.join(path, file_name), "w") as f:
    print(f.write("This is a new line"))


file_path = r"E:\Internship\Python_Practice\pynative_python_exercise\Python_Input_Output_Exercise\sales1.txt"

if os.path.exists:
    print("file is already exists")
else:
    with open(file_path, "w") as f:
        print(f.write("This is first line"))


try:
    with open(file_path, "x") as fp:
        pass
except:
    print("File is already exists")

x = datetime.now()

file_name = x.strftime("%d-%m-%Y-%H-%M-%S.txt")

with open(
    f"E:\Internship\Python_Practice\pynative_python_exercise\Python_Input_Output_Exercise\{file_name}",
    "w",
) as fp:
    print("created", file_name)


os.umask(0)

with open(os.open(file_path, os.O_CREAT | os.O_WRONLY, 0o777), "w") as fh:
    fh.write("content")
