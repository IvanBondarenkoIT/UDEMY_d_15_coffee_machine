import config


def spend_resources(coffe, resources):
    ingredients = coffe["ingredients"]
    for resource in ingredients:
        resources[resource] -= ingredients[resource]


def insert_coins():
    dict_of_coins = config.dict_of_coins
    total_sum = 0
    for coin in dict_of_coins:
        total_sum += dict_of_coins[coin] * int(input(f"how many {coin}?: "))
    return total_sum


def resources_checking(choice, resources):
    # todo 4. Check resources sufficient?
    menu = config.MENU
    ingredients = menu[choice]["ingredients"]
    for resource in ingredients:
        if resources[resource] <= ingredients[resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
    else:
        return True


def make_coffee(choice, resources, money):
    coffe = config.MENU[choice]
    # todo 5. Process coins.
    print("Please insert coins.")
    total_coins = insert_coins()
    # todo 6. Check transaction successful?
    if total_coins < coffe["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    elif total_coins > coffe["cost"]:
        print(f"Here is ${round(total_coins - coffe['cost'],2)} in change.")
    money += coffe['cost']
    spend_resources(coffe, resources)
    # todo 7. Make Coffee.
    print(f"Here is your {user_choice} ☕️. Enjoy!")
    return money


def report(resources, money):
    return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}"


resources = config.resources
money = 0.0
list_of_choices = ["espresso", "latte", "cappuccino", "off", "report"]

while True:
    # todo 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    if user_choice not in list_of_choices:
        print("You choice is incorrect")
        continue
    elif user_choice == "off":
        # todo 2. Turn off the Coffee Machine by entering “off” to the prompt.
        break
    elif user_choice == "report":
        # todo 3. Print report.
        print(report(resources, money))
    else:
        if resources_checking(user_choice, resources):
            money += make_coffee(user_choice, resources, money)