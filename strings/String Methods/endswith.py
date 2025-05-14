# Parameter
# string.endswith(value, start, end)
 
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)


txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)


txt = "Hello, welcome to my castle."
x = txt.endswith(("world.", "castle."))
print(x)











text = "Python programming is easy to learn."

# start parameter: 7
# "programming is easy to learn." string is searched
result = text.endswith('learn.', 7)
print(result)

# Both start and end is provided
# start: 7, end: 26
# "programming is easy" string is searched

result = text.endswith('is', 7, 26)
# Returns False
print(result)

result = text.endswith('easy', 7, 26)
# returns True
print(result)