# Remove the leading and trailing whitespaces from the string:
'''
" hello world! this is PYTHON string methods PRACTICE. "
'''

string_1 = " hello world! this is PYTHON string methods PRACTICE. "
result_1 = string_1.strip()
print(result_1)

#################################################################

# Convert the trimmed string into all lowercase characters:

trimmed_string = "This is the trimmed string."
trimmed_result = trimmed_string.lower()
print(trimmed_result)

#################################################################

# Capitalize only the first character of the string (rest should be lowercase):

string_2 = "this is the mini blog on k8s."
result_2 = string_2.capitalize()
print(result_2)

#################################################################

# Convert the string so that the first character of each word is capitalized.

string_3 = "this is the mini blog on k8s."
result_3 = string_3.title()
print(result_3)