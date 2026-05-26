MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}


while True:
    prompt = input("What would you like to drink?\n")
    if prompt == "report":
        print(resources)
    elif prompt == "off":
        break
    else:

        ingredients = MENU[prompt]["ingredients"]
        can_make = True
        for ingredient, amount in ingredients.items():
            if resources[ingredient] < amount:
                print(f"Sorry, there is not enough {ingredient}.")
                can_make = False
                break
        if can_make:
            count_coins = []
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
            for coin in coins:
                count_coins.append(int(coin))

            quarter, dimes, nickles, pennies = count_coins
            total = (quarter * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

            drink_cost = MENU[prompt]["cost"]
            if total >= drink_cost:
                change = round(total - drink_cost, 2)
                if change > 0:
                    print(f"Here is your {change}")
                print(f"Here is your {prompt}, enjoy it!:")
                for ingredient, amount in ingredients.items():
                    resources[ingredient] -= amount
            else:
                print(f"Sorry, the money is not enough. {total} is refunded.")

