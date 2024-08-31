#Day 4 Project: Rock Paper Scissors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

invalid = '''
⠀⣀⣴⣿⣿⣿⣿⣷⣄⠀
⢸⣿⣿⠋⠁⠀⠉⠛⣿⣿⡆
⠘⣿⣿⣧⠀⠀⠀⠀⠈⣿⣿⡄
⠀⠻⣿⣿⣷⣤⣀⣤⣾⣿⣿⠇
⠀⠀⠈⠙⠻⢿⣿⣿⣿⡿⠋⠀⠀⠀⠀
'''

print("Welcome to the Rock Paper Scissors Game!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors: "))

if user_choice == 0:
    print(f"\nYou chose:\n{rock}")
elif user_choice == 1:
    print(f"\nYou chose:\n{paper}")
elif user_choice == 2:
    print(f"\nYou chose:\n{scissors}")
else: 
    print(f"\nWhat did you even choose? Are you trying to lose?\n{invalid}")

computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print(f"\nComputer chose:\n{rock}")
elif computer_choice == 1:
    print(f"\nComputer chose:\n{paper}")
else:
    print(f"\nComputer chose:\n{scissors}")

# Code to determine who wins:

if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice >= 3:
    print("At least the computer understands the game. You lose!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif user_choice == 0 and computer_choice == 1:
    print("You lose!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose!")
else:
    print("You won!")
