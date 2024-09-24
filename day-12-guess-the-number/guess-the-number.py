# Day 12 Project: The Number Guessing Game

import random
import guess_the_number_art


EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def check_answer(user_guess, number_to_guess, number_of_attempts):
    if user_guess > number_to_guess:
        print("Too high.")
        return number_of_attempts - 1
    elif user_guess < number_to_guess:
        print("Too low.")  
        return number_of_attempts - 1
    else:
        print(f"You got it! The answer is {number_to_guess}.")
            
    
def number_of_attempts():
    user_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if user_level == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif user_level == "hard":
        return HARD_LEVEL_ATTEMPTS

def play_game():
    number_to_guess = random.randint(1, 100)
    
    print(guess_the_number_art.logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
   
    user_attempts = number_of_attempts()
    
    guess = 0
    
    while guess != number_to_guess:
        print(f"You have {user_attempts} attempts remaining to guess the number.")
        
        user_guess = int(input("Make a guess: "))
        
        user_attempts = check_answer(user_guess, number_to_guess, user_attempts)
        if user_attempts == 0:
            print(f"You've run out of guesses, you lose! The answer is {number_to_guess}.")
            return
        elif guess != number_to_guess:
            print("Guess again.")
    
play_game()
 