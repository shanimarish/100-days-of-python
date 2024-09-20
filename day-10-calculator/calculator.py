# Day 10 Project: Calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

should_continue = True

while should_continue:
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    first_num = float(int(input("What's the first number? ")))
    operation_symbol = input("""Pick a mathematical operation!
    Operations: "+", "-", "*" or "/": """)
    second_num = float(int(input("What's the next number? ")))

    answer = operations[operation_symbol](first_num, second_num)
    print(f"{first_num} {operation_symbol} {second_num} = {answer}")

    user_choice = input(f'Type "y" to continue calculating with {answer} or type "n" to start a new calculation. ')

    if user_choice == "y":
        first_num = answer
        operation_symbol = input("""Pick a mathematical operation!
            Operations: "+", "-", "*" or "/": """)
        second_num = float(int(input("What's the next number? ")))
        answer = operations[operation_symbol](first_num, second_num)
        print(f"{first_num} {operation_symbol} {second_num} = {answer}")
    elif user_choice == "n":
        should_continue = False
