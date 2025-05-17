# Check whether the string "Python3" contains only alphanumeric characters.

string_1 = "Python3"
result_1 = string_1.isalnum()
print(result_1)

#################################################################

# Check whether the string "Python3" contains only alphabetic characters.

string_2 = "Python3"
result_2 = string_2.isalpha()
print(result_2)

#################################################################

# Swap the case of each letter in the string "Python3".

string_3 = "Python3"
result_3 = string_3.swapcase()
print(result_3)

#################################################################

# Check whether "Python3" is a valid Python identifier.

string_4 = "Python3"
result_4 = string_4.isidentifier()
print(result_4)

#################################################################

# Pad the string "Python3" with leading zeroes so that its total length becomes 10.

string_5 = "Python3"
result_5 = string_5.zfill(10)
print(result_5)

#################################################################

# Translation

# Replace all vowels in the string "example string" with numbers using maketrans() and translate().

string_6 = "example string"
to_replace = "aeiou"
from_replace = "12345"
table = str.maketrans(to_replace , from_replace)
replaced_string = string_6.translate(table)
print(replaced_string)
