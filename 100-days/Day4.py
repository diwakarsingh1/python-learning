# import random
#
# random_no = random.randint(1,1000)
# print(random_no)
import random

# import random
#
# print(random.random()*10)
#
# random_float = random.uniform(1,30)
# print(random_float)



# import random
#
# print("GAME BEGIN: HEAD and TAIL")
# random_heads_or_tails = random.randint(0,1)
# print(random_heads_or_tails)
# if random_heads_or_tails == 0:
#     print("Its HEAD")
# else:
#     print("Its TAIL")

####################################################################



# List
# states_of_india = ["Uttar Pradesh", "Uttarakhand", "Bihar", "J&K"]
# states_of_india[1] = "Punjab"
# states_of_india.extend(["haryana", "Gujrat"])
# states_of_india.insert(2, "Diwakar")
# states_of_india.pop(2)
# states_of_india.remove("Uttar Pradesh")
# print(states_of_india)


# friend_list = ["Aryan" , "Dushyant" , "Navneet" , "Manas" , "Harsh"]
# total_friends = len(friend_list)
# who_will_pay_the_bill = random.randint(0, total_friends-1)
# print(who_will_pay_the_bill)
# print(friend_list[who_will_pay_the_bill])
# print(total_friends)

# friend_list = ["Aryan" , "Dushyant" , "Navneet" , "Manas" , "Harsh" , "kukki"]
# print(random.choice(friend_list))

# fruits = ["Apple" , "Banana" , "Orange" , "Grapes" , "Watermelon"]
# vegetables = ["Brinjal" , "Pumpkin" , "Loki" , "Torai"]
#
# nutrition_foods = [fruits , vegetables]
# print(nutrition_foods)
# print(nutrition_foods[0])
# print(nutrition_foods[1])
# print(nutrition_foods[1][3])

# Rock Paper Scissor

# rock = '''
# _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
# paper = '''
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# '''
# scissor = '''
# _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# images = [rock, paper, scissor]
#
# users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor: \n"))
# computer_choice  = random.randint(0 , 2)
# if users_choice >=0 and users_choice <=2:
#     print(f"user choice: {users_choice}")
#     print(images[users_choice])
#
# print(f"computer choice: {computer_choice}")
# print(images[computer_choice])
#
#
# if users_choice >= 3 or users_choice < 0:
#     print("You choose an invalid number, you loose.")
# elif users_choice == 0 and computer_choice == 2:
#     print("You Wins !!!! ")
# elif computer_choice == 0 and users_choice == 2:
#     print("you loose")
# elif computer_choice > users_choice:
#     print("You looses !!!!")
# elif users_choice > computer_choice:
#     print("you win")
# elif computer_choice == users_choice:
#     print("Its draw")













