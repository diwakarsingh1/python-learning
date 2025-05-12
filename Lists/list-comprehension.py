list = ["Diwakar" , "Singh" , "Prajapati"]
copy_list = []
for x in list:
    copy_list.append(x)
print(copy_list)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# with list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

# fruits = ['apple', 'banana', 'cherry']
# newlist = [x for x in fruits if x == 'banana']
# print(newlist)