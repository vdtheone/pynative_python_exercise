# Initialize dictionary with default values

# In Python, we can initialize the keys with the same values.


employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

data = {}

for i in employees:
    data[i] = defaults


print(data)

res = dict.fromkeys(employees, defaults)
print(res)