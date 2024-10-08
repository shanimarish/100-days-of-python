# Day 4 Project: Rock Paper Scissors

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

game_ascii_art = [rock, paper, scissors]

print("Welcome to the Rock Paper Scissors Game!")

# User Choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors: "))
if user_choice >= 0 and user_choice <= 2:
    print(f"\n You chose:\n{game_ascii_art[user_choice]}")
else: 
    print(f"\nWhat did you even choose? Are you trying to lose?\n{invalid}")

# Computer Choice
computer_choice = random.randint(0, 2)
print(f"Computer chose:\n{game_ascii_art[computer_choice]}")

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
