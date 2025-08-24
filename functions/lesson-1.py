import time
import random
drink = "Available"
food = input(random.choice(["Pizza", "Burger", "Pasta"]))
def new_menu(item):
    if item == drink:
        print(drink)
    else:
        print("What do you want to eat today?")

        food = input()
        print("cooking in progress...")
        time.sleep(5)
        print(f"{food} is ready to serve!")
new_menu(drink)
new_menu(food) 