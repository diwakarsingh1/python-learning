#parameter

# string.format_map(dictionary)

myVar = {"name" : "Diwakar Singh" , "Age" : 29}
txt = "happy birthday {name} you are now at level {Age}"
print(txt.format_map(myVar))