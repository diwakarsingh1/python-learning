# Split the lowercase version of the string into a list of words.

string_1 = 'This is the only way to learn AWS.'
converted_string = string_1.lower()
result_1 = converted_string.split(" ")
print(result_1)

#################################################################

# Join the words back with '_' in between

string_2 = ("This" , "is" , "the" , "AWS" , "Practitioner" ,  "Exam" ,  "index.")
joining_char = "_"
joined_string = joining_char.join(string_2)
print(joined_string)



# Split string by line breaks (create a multi-line string first)

string_3 = "This is the only way to love the nature.\nOtherwise there are so much places to love it in the imagination.\nNot only in imagination but also in reality"
result_3 = string_3.splitlines()
print(result_3)