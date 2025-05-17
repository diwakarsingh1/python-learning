# parameter
# string.rstrip(characters to remove)


txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")


txt = "banana,,,,,ssqqqww....."

x = txt.rstrip(",.qsw")

print(x)