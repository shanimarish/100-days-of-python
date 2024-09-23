# Day 11 Project: Blackjack

import random
import blackjack_art

def deal_card():
    """
    Returns a random card from the deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(cards):
    """
    Take a list of cards and return the score calculated from
    the cards to user_score and computer_score
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    """
    Compare user cards and computer cards to see who wins
    """
    if u_score == c_score:
        return "It's a draw!"
    elif c_score == 0:
        return "Opponent has a Blackjack! You lose!"
    elif u_score == 0:
        return "You won with a Blackjack!"
    elif u_score > 21:
        return "You went over 21! You lose!"
    elif c_score > 21:
        return "Opponent went over 21. You won!"
    elif u_score > c_score:
        return "You won!"
    else:
        return "You lose!"

def play_game():
    """
    This is basically the Blackjack game!
    """
    print(blackjack_art.logo)

    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input("Do you want do draw another card? Type 'yes' or 'no': ").lower()
            if user_choice == "yes":
                user_cards.append(deal_card())
            elif user_choice == "no":
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\n\nYour final hand is {user_cards} and your final score is {user_score}.")
    print(f"The opponent's final hand is {computer_cards} and the final score is {computer_score}.")
    print(compare(user_score, computer_score))

def start_game():
    should_continue = True
    while should_continue:
        user_play = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower()
        if user_play == "yes":
            print("\n" * 20)
            play_game()
        elif user_play == "no":
            should_continue = False
        else:
            print("\nInvalid input. Please type 'yes' or 'no'.")
start_game()
