# x = 1
# y = 35656222554887711
# z = -3255522

# print(type(x))
# print(type(y))
# print(type(z))

# x = 3+5j
# y = 5j
# z = -5j

# print(type(x))
# print(type(y))
# print(type(z))

# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# #convert from int to float:
# a = float(x)

# #convert from float to int:
# b = int(y)

# #convert from int to complex:
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))



# import random

# print(random.randrange(1, 10))


# txt = "Hello, welcome to my world."

# x = txt.find("e", 5, 10)

# print(x)


# x = 5.5
# y = int(x)
# print(round(y))
# print(int(35.98))

# print(bool("abc"))


# x = range(6)

# #display x:
# print(x)

# #display the data type of x:
# print(type(x)) 

# x = frozenset({"apple", "banana", "cherry"})
# print(x)

# x = bytearray(5)
# print(x)        # Output: bytearray(b'\x00\x00\x00\x00\x00')
# print(type(x)) 
# for x in "banana":
#   print(x)

# b = "Hello, World!"
# print(b[-5:-2])

# age = 36
# txt = (f"My name is John, I am  {age}")
# print(txt)


# def myFunction() :
#   return True

# if myFunction():
#   print("YES!")
# else:
#   print("NO!")



x = "200"
print(isinstance(x, str))


# # Reading input until user types "exit"
# while (user_input := input("Enter something: ")) != "exit":
#     print(f"You typed: {user_input}")


choice = input("Enter something: ")
while choice != "exit":
    print(f"You type: {choice}")
    choice = input("Enter something: ")