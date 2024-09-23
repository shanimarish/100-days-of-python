# Day 12 Project: The Number Guessing Game

import random
import guess_the_number_art

def random_number():
    return random.randint(1, 100)

def number_of_attempts(attempt):
    if attempt == "easy":
        return 10
    elif attempt == "hard":
        return 5

number_to_guess = random_number()

def play_game():
    print(guess_the_number_art.logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
       
    user_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    user_attempts = number_of_attempts(user_level)
    while user_attempts > 0:
        print(f"You have {user_attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess == number_to_guess:
            print(f"You got it! The answer is {number_to_guess}.")
            return
        elif user_guess > number_to_guess:
            print("Too high.")
        elif user_guess < number_to_guess:
            print("Too low.")  
            
        user_attempts -= 1
        if user_attempts > 0:
            print("Guess again.")
        
    print(f"You've run out of guesses, you lose! The answer is {number_to_guess}.")
    
play_game()
 