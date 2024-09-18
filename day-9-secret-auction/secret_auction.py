# Day 9 Project: Secret Auction

import secret_auction_art
print(secret_auction_art.logo)

def blind_auction(bidding_list):
    greatest_bid = 0
    greatest_bidder = ""

    for bidder in bidding_list:
        bid = bidding_list[bidder]
        if bid > greatest_bid:
            greatest_bid = bid
            greatest_bidder = bidder
    print(f"The winner is {greatest_bidder} with a bid of ${greatest_bid}.")

bidding_dictionary = {}

new_bidder = True
while new_bidder:
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: $"))
    bidding_dictionary[user_name] = user_bid

    user_choice = input("Are there any other bidders? Type yes or no: ").lower()
    if user_choice == "no":
        new_bidder = False
        blind_auction(bidding_dictionary)
    elif user_choice == "yes":
        print("\n" * 100)
