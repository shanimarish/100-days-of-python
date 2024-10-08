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
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}ml")
        print(f"Money: {resources["money"]} pesos")
        return
    
    if coffee_drink in MENU:
        ingredients = MENU[coffee_drink]["ingredients"]
        
        for item in ingredients:
            if ingredients[item] > resources.get(item, 0):
                print(f"Sorry, there is not enough {item}.")    
                return 
        process_coins(coffee_drink)
    else:
        print("Sorry, that drink is not on the menu.")
        return 
    
def process_coins(drink_name):
    """Compute the right amount of money for the drink."""
    drink_cost = MENU[drink_name]["cost"]
    
    print(f"The {drink_name} costs {drink_cost} pesos.")
    user_money = int(input("How much will you pay? "))
    
    
    if user_money < drink_cost:
        print(f"Sorry, that's not enough money to buy {drink_name}. Money refunded!")
        return
    elif user_money > drink_cost:
        user_change = user_money - drink_cost
        print(f"Here is {user_change} pesos in change.")
        resources["money"] += drink_cost   
        make_coffee(drink_name)  
    else:
        resources["money"] += drink_cost  
        make_coffee(drink_name) 

def make_coffee(drink_resources):
    """Deduct the coffee ingredients from the resources."""
    ingredients = MENU[drink_resources]["ingredients"]
    
    print(f"""
              Report before purchasing latte:
              Water: {resources["water"]}ml
              Milk: {resources["milk"]}ml
              Coffee: {resources["coffee"]}ml
            """)
    
    for item in ingredients:
        resources[item] -= ingredients[item]
        
    print(f"""
              Report after purchasing latte:
              Water: {resources["water"]}ml
              Milk: {resources["milk"]}ml
              Coffee: {resources["coffee"]}ml
            """)
    print(f"Here is your {drink_resources}. Enjoy!")

def coffee_machine():
    """Make the coffee order."""
    should_continue = True 
    
    while should_continue != False:
        user_input = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    
        if user_input == "off":
            print("Turning off the coffee machine. Goodbye!")
            should_continue = False
        else:
            check_resources(user_input)
            
        if should_continue:
            another_order = input("Do you want to order again? Type 'y' or 'n': ").lower()
            if another_order == "y":
                user_input = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
                check_resources(user_input) 
            else: 
                print("Thank you for your order. Bye!")
                should_continue = False
            
coffee_machine()
