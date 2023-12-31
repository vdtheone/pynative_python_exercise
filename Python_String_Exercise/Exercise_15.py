# Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

data = []

for i in str_list:
    if i:
        data.append(i)

print(data)

new_str_list = list(filter(None, str_list))

print(new_str_list)
