"""Component 3 -- Version 3 -- trial 1
Print correct money in the correct currency and the right decimal points
Removing unnecessary print statements
Instead the amount of times repeated to 500 to get more fair and accurate results.
I made it harder to get unicorn -- only a 12.5% chance
Easier to get a zebra or horse -- a 25% chance
and much easier to get Donkey -- 37.5% chance
-- This code works, but I think I can get it better so my house is MORE likely to win/gain more money.
By Katelyn Gee
10/04/2022"""

# makes the random function accessible
import random

# list of animals for computer to randomly choose
animals = ["Zebra", "Zebra", "Unicorn", "Horse", "Horse", "Donkey", "Donkey", "Donkey"]

# Starting variables
STARTING_BALANCE = 100
money = STARTING_BALANCE

# computer chooses a random animal 20 times and printing it
for i in range(10):
    computer_choice = random.choice(animals)
    # Lose money to play game
    money -= 1

    # Loses or gains money depending on the token
    if computer_choice == "Zebra" or computer_choice == "Horse":
        money_gained = 0.5
        money += money_gained

    elif computer_choice == "Unicorn":
        money_gained = 5
        money += money_gained

    else:
        money_gained = 0

print(f"You starting balance was {STARTING_BALANCE:.2f} ")
print("---------------------------------------")
print(f"You final balance is ${money:.2f}")



