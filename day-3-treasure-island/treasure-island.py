#Day 3 Project: Treasure Island

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

user_direction = input('\nWhere do you want to go? Do you want to walk "left" or "right"?: ').lower()
if user_direction == "left":
    user_action = input('\nAwesome! You found a river. Do you want to "swim" or "wait"?: ').lower()
    if user_action == "wait":
        user_house_color = input('\nSomeone saw you and offer you to ride the boat! \nHe dropped you off to an island with three mysterious houses. \nShould you go inside the "red", "yellow", or "blue" house?: ').lower()
        if user_house_color == "red":
            print("\nAn arsonist burned the house while you're inside. Game over!")
        elif user_house_color == "blue":
            print("\nThe lights went off and next thing you know is that you're eaten by beasts. Game over!")
        else:
                print("\nYay! You found the treasure. You win!")
                print('''
                *******************************************************************************
                          |                   |                  |                     |
                 _________|________________.=""_;=.______________|_____________________|_______
                |                   |  ,-"_,=""     `"=.|                  |
                |___________________|__"=._o`"-._        `"=.______________|___________________
                          |                `"=._o`"=._      _`"=._                     |
                 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
                |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
                |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
                 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
                |                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
                |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
                ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
                /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
                ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
                /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
                ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
                /______/______/______/______/______/______/______/______/______/______/_____ /
                *******************************************************************************
                ''')
    else:
        print("\nDamn! You're attacked by a trout? It's game over.")
else:
        print("\nOh no! You fall into a hole. Game over.")
