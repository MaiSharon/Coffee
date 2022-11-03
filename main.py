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


def calculator():
    coins_enough = True
    while coins_enough:
        print("Please insert coins.")
        quarters = int(input("how many quarters?"))
        dimes = int(input("how many dimes?"))
        nickles = int(input("how many nickles?"))
        pennies = int(input("how many pennies?"))
        total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        # TODO 錢太多要找錢
        if total >= 2.5:
            change = total - 2.5
            print(f"Here is ${change} in change.")
            coins_enough = False
            return 2.5
        # TODO 確認錢夠嗎
        else:
            print("Sorry that's not enough money. Money refunded. ")
            return 0


def check_food_(what_food, food):
    """輸入當前原物料與使用者要用掉的原物料"""
    what_food -= food
    return what_food


# TODO need loop
coffee_open = True
coins = 0
while coffee_open:

    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = coins

    # TODO ask user's drink
    choose = input(" What would you like? (espresso/latte/cappuccino)")
    # 運算原物料夠不夠
    if choose == 'espresso' or choose == 'latte' or choose == 'cappuccino':
        # TODO 給完咖啡後原物料還剩多少
        for key in MENU[choose]["ingredients"]:
            food = MENU[choose]["ingredients"][key]
            if key == "water":
                water = check_food_(water, food)
            elif key == "milk":
                milk = check_food_(milk, food)
            elif key == "coffee":
                coffee = check_food_(coffee, food)

        # TODO 確認原物料夠嗎
        if water < 0:
            print(" Sorry there is not enough water")
        elif milk < 0:
            print(" Sorry there is not enough milk")
        elif coffee < 0:
            print(" Sorry there is not enough coffee")
        else:
            # 先確認使用者錢有沒有付夠，再進行原物料製作
            coins += calculator()
            if coins == money:
                continue
            # 製作並更新剩餘原物料
            resources["water"] = water
            resources["milk"] = milk
            resources["coffee"] = coffee
            print(f"Here is your {choose}. Enjoy!")

    # TODO print report
    if choose == "report":
        print(f"Water: {water}")
        print(f"Coffee: {coffee}")
        print(f"Milk: {milk}")
        print(f"Money: ${money}")
    # TODO input "off" need to end
    if choose == "off":
        coffee_open = False

# TODO 錢的計算
# choose = input(" What would you like? (espresso/latte/cappuccino)")
