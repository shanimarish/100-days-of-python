# Day 15 Project: Coffee Machine 

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 100,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 150,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def check_resources(coffee_drink):
    """Check if there are sufficient resources to make the drink."""
    if coffee_drink == "report":
        report_resources()
        return
    
    if coffee_drink in MENU:
        ingredients = MENU[coffee_drink]["ingredients"]    
        for item in ingredients:
            if ingredients[item] > resources.get(item, 0):
                print(f"Sorry, there is not enough {item}.")    
                return False
        return True
    else:
        print("Sorry, that drink is not on the menu.")
        return False
    
def report_resources():
    """Print the resources available."""    
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: {resources["money"]} pesos")
        
def process_coins(drink_name):
    """Compute the right amount of money for the drink."""
    drink_cost = MENU[drink_name]["cost"]
    print(f"The {drink_name} costs {drink_cost} pesos.")

    # Ask the user to input the number of each type of coin.
    one_peso = int(input("How many 1 peso coins? "))
    five_peso = int(input("How many 5 peso coins? "))
    ten_peso = int(input("How many 10 peso coins? "))
    twenty_peso = int(input("How many 20 peso coins? "))

    # Calculate the total money inserted.
    user_money = (one_peso * 1) + (five_peso * 5) + (ten_peso * 10) + (twenty_peso * 20)
    print(f"Total inserted: {user_money} pesos.")

    # Check if the user inserted enough money.
    if user_money < drink_cost:
        print(f"Sorry, that's not enough money to buy {drink_name}. Money refunded!")
        return False
    elif user_money > drink_cost:
        user_change = round(user_money - drink_cost, 2)
        print(f"Here is {user_change} pesos in change.")
        resources["money"] += drink_cost   
        return True 
    else:
        resources["money"] += drink_cost  
        return True

def make_coffee(drink_resources):
    """Deduct the coffee ingredients from the resources."""
    ingredients = MENU[drink_resources]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_resources}. Enjoy!")

def coffee_machine():
    """Make the coffee order."""
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_input == "off":
            print("Turning off the coffee machine. Goodbye!")
            break
        
        if user_input == "report":
            report_resources()
            continue 

        if check_resources(user_input):
            if process_coins(user_input):
                make_coffee(user_input)
            
coffee_machine()
