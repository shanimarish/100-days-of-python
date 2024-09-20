# Day 7 Project: Hangman

import random
import hangman_art
import hangman_words
print(hangman_art.logo)

lives = 6
chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
for letter_position in range(0, len(chosen_word)):
    placeholder += "_"
print(f"\nWord to guess: {placeholder}")

correct_letters = []

game_over = False
while not game_over:
    print(f"\n\n****************************{lives}/6 LIVES LEFT****************************")
    guess = str(input("\nGuess a letter: ")).lower()

    if guess in correct_letters:
        print(f"You've already guess {guess}.")  
    
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            
    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess} and that's not in the word. You lose a life.")
        if lives == 0:
            print(f'***********************YOU LOSE! The correct word is "{chosen_word}."**********************')
            game_over = True
    
    print(hangman_art.stages[lives])
        
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
    