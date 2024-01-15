# Sort a tuple of tuples by 2nd item

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

sorted_tuple = tuple(sorted(tuple1, key=lambda k:k[1]))

print(sorted_tuple)