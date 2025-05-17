# parameter
# string.rsplit(separator, maxsplit)

txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)

txt = "apple, banana, cherry"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)

print(x)