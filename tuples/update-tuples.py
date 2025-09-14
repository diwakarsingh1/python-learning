# Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "pineapple"
x = tuple(y)

print(x)



thistuple = ("apple", "banana", "cherry")
thisList = list(thistuple)
thisList.append("pineapple")
thistuple = tuple(thisList)
print(thistuple)


thisTuple = ("apple" , "banana" , "cherry")
y = ("mango",)
thisTuple += y
print(thisTuple)


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)