#print("Diwakar"[4])

#print(type(True))

#print("Number of letters in your name: " + str(len(input("Enter Your name:"))))


# name_of_the_user = input("Enter your name: ")
# length_of_name = len(name_of_the_user)
# print("Number of letters in your name: " + str(length_of_name))

# print(3 * 3 + 3 / 3 - 3)

# Height = int(input("Enter your Height:"))
# Weight = int(input("Enter your Weight:"))
# BMI = (Weight/(Height ** 2))
# print(BMI)


# x = input("Enter a number: ")
# print(type(x))


# a = 10
#
# a+=1
# print(a)
#
#
# height = 10
# weight = 20
# you_are_good = True
#
#
# print(f"Your Height is {height}, your weight is {weight}. You are good {you_are_good}")
# print("Your Height is " + str(height) + ", your weight is " +  str(weight) + ". You are good " +  str(you_are_good))
#
# a = int("5") / int(2.7)
# print(a)

# age = 12
# print(type(age))

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10 ,12, or 15?"))
people = int(input("How many people to split the bill?"))
bill_after_tip = (bill + (bill*tip)/100)
total_bill = round((bill_after_tip/people), 2)
print(f"Each person should pay: $ {total_bill}")






