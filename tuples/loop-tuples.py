print("Simple loop")
thisTuple = ("apple", "banana", "cherry")
for x in thisTuple:
    print(x)


print("using indexing")
thisTuple = ("apple", "banana", "cherry")
for x in range(len(thisTuple)):
    print(thisTuple[x])


print("Using while loop")
thisTuple = ("apple", "banana", "cherry")
i = 0
while i < len(thisTuple):
    print(thisTuple[i])
    i = i + 1
