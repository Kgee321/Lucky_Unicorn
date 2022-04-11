"""Component 3 -- Version 2
Code starts with $100 and only gains money when a unicorn is generated
-- Although this code has a problem, the balance increases instead of decreases like it is meant to.
By Katelyn Gee
7/04/2022"""

# makes the random function accessible
import random

# list of animals for computer to randomly choose
animals = ["Zebra", "Unicorn", "Horse", "Donkey"]

# Starting variables
money = 100

# computer chooses a random animal 20 times and printing it
for i in range(20):
    computer_choice = random.choice(animals)
    # Lose money to play game
    money -= 1
    # print computer choice
    print(computer_choice)

    # Loses or gains money depending on the token
    if computer_choice == "Zebra" or computer_choice == "Horse":
        money_gained = 0.5
        money += money_gained

    elif computer_choice == "Unicorn":
        money_gained = 5
        money += money_gained

    else:
        money_gained = "nothing"

    print(f"You gained {money_gained}, \nYour balance is now {money}")
    print()
print("---------------------------------------")
print(f"You final balance is {money}")



