MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "cash": 0,
}

# TODO: 1. Print a report of all coffee machine resources

def report(resources):
    print(f'Water: {resources["water"]}')
    print(f'Milk: {resources["milk"]}')
    print(f'Coffee: {resources["coffee"]}')
    print(f'Cash: {resources["cash"]}')

# report(resources)


# A Function that makes beverages
def beverage(MENU, resources, primary_question):
    available_water = resources["water"]
    required_water = MENU[primary_question]["ingredients"]["water"]

    available_coffee = resources["coffee"]
    required_coffee = MENU[primary_question]["ingredients"]["coffee"]

    available_milk = resources["milk"]
    required_milk = MENU[primary_question]["ingredients"]["milk"]



    if resource_check(available_water, required_water, available_coffee, required_coffee, available_milk, required_milk) == True:
        print("Please insert coins.")
        coins_input = coin_processing(MENU, resources)
        # TODO 6. Check transaction successful. (did they input enough coins)
        if coins_input >= MENU[primary_question]["cost"]:
            print(f"{primary_question.capitalize()} was produced.")

            resources["coffee"] = resources["coffee"] - MENU[primary_question]["ingredients"]["coffee"]
            resources["water"] = resources["water"] - MENU[primary_question]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU[primary_question]["ingredients"]["milk"]

            change = coins_input - MENU[primary_question]["cost"]
            resources["cash"] = resources["cash"] + MENU[primary_question]["cost"]
            print(f"Your change is ${round(change, 2)}")
        elif coins_input < MENU[primary_question]["cost"]:
            print(f"That's not enough for a {primary_question}.\nReturning ${coins_input}")


# TODO: 4. Check resources sufficient
def resource_check(available_water, required_water, available_coffee, required_coffee, available_milk, required_milk):
    if available_water >= required_water and available_coffee >= required_coffee and available_milk >= required_milk:
        print("[Sufficient resources are available.]")
        return True
    else:
        if available_water < required_water:
            print("Resource levels insufficient: Water")


        if available_coffee < required_coffee:
            print("Resource levels insufficient: Coffee")


        if available_milk < required_milk:
            print("Resource levels insufficient: Milk")
        return False

# TODO 5. Process coins/coin input
def coin_processing(MENU, resources):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    qvalue = float(quarters) * 0.25
    dvalue = float(dimes) * 0.10
    nvalue = float(nickels) * 0.05
    pvalue = float(pennies) * 0.01

    total_coins = qvalue + dvalue + nvalue + pvalue
    total_coinsr = round(total_coins, 2)

    print(f"Total coins inserted come to: ${total_coinsr}")
    return total_coinsr

# print(MENU["espresso"]["ingredients"]["water"])
primary_question = 0

# TODO: 3. Turn off coffee machine by entering 'off' to the prompt. DONE
while primary_question != "off".lower():
    # TODO: 2. Prompt user by asking "What would you like? (espresso/latte/cappucino)"
    primary_question = input("What would you like? (espresso/latte/cappuccino)(off/report/refill): ").lower()


    if primary_question == "espresso" or primary_question == "latte" or primary_question == "cappuccino":
        beverage(MENU, resources, primary_question)

    elif primary_question == "report":
        report(resources)

    elif primary_question =="refill":
        fill_amount = 200
        resources["coffee"] = resources["coffee"] + (fill_amount / 2)
        resources["water"] = resources["water"] + fill_amount
        resources["milk"] = resources["milk"] + fill_amount

    elif primary_question == "off":
        primary_question = "off"
    else:
        primary_question = input("Invalid input.\nWhat would you like? (espresso/latte/cappuccino)(off/report): ").lower()















