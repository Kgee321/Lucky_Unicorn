"""Component 3 -- Version 3 -- trial 2
I made it harder to get unicorn -- only a 5% chance of getting a unicorn
Easier to get a zebra or horse -- a 65% chance of getting either of them (32.5% each or as close to that as I can get)
and much easier to get Donkey -- 30% chance
It does this my choosing a random number and printing a token depending on what the number is.
I also changed the amount of times it is repeat back to 10 for practical reasons.
It is mostly a lost but sometimes, it is a slight win so then players want to play again/continue playing.
By Katelyn Gee
10/04/2022"""

# makes the random function accessible
import random

# Starting variables
STARTING_BALANCE = 100
money = STARTING_BALANCE

for i in range(10):
    # Take off $1 to play the game
    money -= 1
    # Computer choice a random
    computer_choice = random.randint(1, 100)
    if computer_choice <= 5:

        # There is a 5% chance the random number will be under 5. If that happens, unicorn is token
        final_choice = "Unicorn"
        money += 5
    elif 6 >= computer_choice >= 35:

        # There is a 30% chance the random number will be between 6 and 35. If that happens, Donkey is token
        final_choice = "Donkey"
    else:
        # Making a list to print a random of zebra or horse
        random_token = ["Zebra", "Horse"]

        # token is randomly selected from horse or zebra
        final_choice = random.choice(random_token)
        money += 0.5

    # prints the token and final money count of each token for testing
    print(f"Your token: {final_choice}, Your balance is now {money}")
    print()

# Print the start balance and what the user ended with
print(f"You starting balance was {STARTING_BALANCE:.2f} ")
print("---------------------------------------")
print(f"You final balance is ${money:.2f}")
