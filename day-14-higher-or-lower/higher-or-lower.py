# Day 14 Project: Higher or Lower 

import random
import higher_or_lower_art
import higher_or_lower_data

def data_picker():
    """Selects a random artist from the dataset."""
    artist_data = higher_or_lower_data.data
    random_artist = random.choice(artist_data)
    return random_artist

user_score = 0

def play_game(artist_a = None, show_score = False):
    """Plays a round of the game."""
    global user_score
    
    if artist_a is None:
        artist_a = data_picker()
        
    artist_b = data_picker()
    
    # Ensure artist_a and artist_b are not identical.
    while artist_a == artist_b:
        random_artist_b = data_picker
    
    random_artist_a = f"{artist_a["name"]}, a {artist_a["description"]}, from {artist_a["country"]}."
    random_artist_b = f"{artist_b["name"]}, a {artist_b["description"]}, from {artist_b["country"]}."

    artist_a_followers = artist_a["follower_count"]
    artist_b_followers = artist_b["follower_count"]
    
    print(higher_or_lower_art.logo)
    
    # Print score message after the first round
    if show_score:
        print(f"You're right! Current score: {user_score}")
        
    print(f"Compare A: {random_artist_a}")
    print(higher_or_lower_art.vs)
    print(f"Against B: {random_artist_b}")
    
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    # Validate user choice
    while user_choice not in ['A', 'B']:
        user_choice = input("Invalid choice. Please type 'A' or 'B': ").upper()
    
    if user_choice == "A":
        if artist_a_followers > artist_b_followers:
            user_score += 1
            print("\n" * 20)
            play_game(artist_b, show_score = True)
        else:
            print(f"Sorry, that's wrong. Final Score: {user_score}")
    elif user_choice == "B":
        if artist_b_followers > artist_a_followers:
            user_score += 1
            print("\n" * 20)
            play_game(artist_b, show_score = True)
        else:
            print(f"Sorry, that's wrong. Final Score: {user_score}")
            
play_game()
