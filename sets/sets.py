myset = {"apple" , "banana" , "cherry"}
print(myset)


# Duplication not allowed, unordered, unchangeable

myset1 = {"apple" , "banana" , "cherry" , "apple"}
print(myset1)


# True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", 1, True, 2}

print(thisset)

# False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)


# length of the set

this_set = {"apple", "banana", "cherry"}
print(len(this_set))
print(type(this_set))

# Set constructor

thisConstructorSet = set(("apple" , "banana" , "cherry"))
print(thisConstructorSet)