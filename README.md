
# ☕ Coffee Machine Simulator

This project is a Python-based command-line simulation of a coffee machine. It allows users to select from a menu of popular coffee drinks, process payments using virtual coins, and manage resources like water, milk, and coffee. The goal is to provide a hands-on demonstration of basic programming concepts such as functions, loops, conditionals, and dictionaries.

---

## 📁 Project Overview

```
coffee-machine/
├── .gitattributes       # Git settings
└── main.py              # Main application logic
```

---

## 🔧 Features

- Choose from three drinks: **Espresso**, **Latte**, or **Cappuccino**
- Simulate coin-based transactions
- Monitor and update inventory resources
- Handle insufficient resources or payment
- Generate a machine status report
- Turn off the machine via command

---

## 🧠 Code Breakdown

### `main.py`

The entire coffee machine logic resides in this file.

---

### 📦 Data Structures

```python
MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0}
}

resources = {"water": 300, "milk": 200, "coffee": 100}
```

- `MENU`: Defines each drink’s ingredients and price
- `resources`: Represents the current inventory available in the machine

---

### 🛠 Functional Overview

#### `clear()`
```python
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
```
Clears the terminal for a cleaner user interface.

---

#### `is_resource_sufficient(order_ingredients)`
```python
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True
```
Checks whether the current inventory is enough to fulfill the drink order.

---

#### `process_coins()`
```python
def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total
```
Accepts virtual coins as payment and calculates the total amount entered.

---

#### `is_transaction_successful(money_received, drink_cost)`
```python
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False
```
Validates if the user has inserted enough money, returns change, and tracks total profit.

---

#### `make_coffee(drink_name, order_ingredients)`
```python
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")
```
Deducts the necessary ingredients from the inventory and simulates dispensing the drink.

---

### 🔄 Main Control Loop

```python
profit = 0
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid selection. Please choose a valid option.")
```

- Manages the continuous operation of the machine
- Accepts user inputs and routes them through the appropriate logic
- Provides real-time feedback for each transaction

---

## ▶️ Getting Started

### 📦 Requirements

- Python 3.x

### 🚀 Run the Program

Clone the repository and run:

```bash
git clone https://github.com/psyccho00/coffee-machine.git
cd coffee-machine
python main.py
```

---

## 📊 Example Usage

```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $0.0 in change.
Here is your latte ☕. Enjoy!
```

---

## 👨‍💻 Author

Developed by [psyccho00](https://github.com/psyccho00)

---

Enjoy a freshly brewed virtual coffee! ☕
