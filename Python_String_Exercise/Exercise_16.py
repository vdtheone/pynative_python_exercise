# Remove special symbols / punctuation from a string

import string

str1 = "/*Jon is @developer & musician"

test_str = str1.translate(str.maketrans('', '', string.punctuation))
print(test_str)