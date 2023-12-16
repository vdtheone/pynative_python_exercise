# Check file is empty or not

import os 

size = os.stat(r'E:\Internship\Python_Practice\pynative_python_exercise\data.txt').st_size

if size == 0:
    print('file is empty')