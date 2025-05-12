# fruits = ["Apple" , "Banana" , "Pear"]
# for fruit in fruits:
#     print(fruit)
import random
from weakref import finalize

# student_score = [150 , 132 , 43 , 123 , 197 , 265 , 235 , 32 , 134]
# total_number = sum(student_score)
# maxi_no = max(student_score)
# print(total_number)
# print(maxi_no)

# sum = 0
# for score in student_score:
#     sum += score
#     print(sum)

# max_score = 0
# for maximum in student_score:
#     if maximum > max_score:
#         max_score = maximum
# print(max_score)

# for number in range(1 , 11 , 3):
#     print(number)

# total = 0
# for number in range(1,101):
#     total += number
# print(total)


# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print (i)



print("Welcome to password generator!")
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']


total_alphabets = int(input('Enter total alphabets you need: '))
total_numbers = int(input("Enter total number of numbers you need: "))
total_special_chars = int(input("Enter total number of special characters you need: "))

password = []
for char in range(0 , total_alphabets):
    password.append(random.choice(alphabets))
for num in range(0 , total_numbers):
        password.append(str(random.choice(numbers)))
for char in range(0 , total_special_chars):
    password.append(random.choice(special_chars))
print(password)
random.shuffle(password)
print(password)

final = ""
for char in password:
    final += char
print(final)
# final_pass = ""
# pass_len = len(password)
# for final_password in range(0,pass_len):
#     final_pass += random.choice(password)
# print(final_pass)






















