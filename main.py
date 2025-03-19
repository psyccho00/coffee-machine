menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 190,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 195,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 275,
    }
}

def is_resource_sufficient(u_input):
    for items in u_input:
        if u_input[items] >= resources[items]:
            print(f"Sry we dont have enough {items}.")
            return False
    return True

def process_money():
    print(" ***** Plz insert coin! ***** ")
    note=int(input("Insert note: "))
    coin=int(input("Insert coins: "))
    total= note+coin
    return total

def transition(money_given,cost_of_item):
    if money_given >= cost_of_item:
        cash_back= money_given-cost_of_item
        global price
        price +=cost_of_item
        print(f"Here,s your change {cash_back}")
        return True

    else:
        print("Not enough money")
        return False

def make_coffee(chosen_drink,ingredients):
    for items in ingredients:
        resources[items] -= ingredients[items]
    print (f" **** Thnx for waiting, Here,s ur {user_input} ****")


price= 0
resources = {
    "water": 900,
    "milk": 800,
    "coffee": 700,
}

machine_off = False

while not machine_off:
    user_input= input("would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        machine_off = True

    elif user_input == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: Rs {price}")

    else:
        drink= menu[user_input]
        if is_resource_sufficient(drink["ingredients"]):
            x = menu[user_input]["cost"]
            print(f"You need to pay Rs {x}")
            payment = process_money()
            transition(payment,x)
            print(".\n"*4)
            print(f" **** plz wait ur {user_input} is being prepared **** ")
            make_coffee(drink,resources)
