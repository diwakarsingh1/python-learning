#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
# string.translate(table)

mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))