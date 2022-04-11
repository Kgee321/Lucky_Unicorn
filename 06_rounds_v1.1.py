"""Component 4 -- Version 1
Using 05_random_v3_trial2 and using a balance of $5 to test it.
Adding the number of rounds and asking the user if they want to continue playing or quit.
Changing the range of random numbers able to be chosen so only donkey can be chosen
-- This is so I can efficiently test my code.
By Katelyn Gee
11/04/2022"""

# makes the random function accessible
import random

# Starting variables
STARTING_BALANCE = 5
money = STARTING_BALANCE
rounds = 0
play_again = ""

while play_again != "x":
    if rounds <= 4:
        # adding one to rounds to make it the right round number
        rounds += 1

        # output the round it is
        print("--------------------------------------------------")
        print()
        print(f"Round {rounds}:")
        print()

        # Take off $1 to play the game
        money -= 1
        # Computer choice a random
        computer_choice = random.randint(6, 36)
        if computer_choice <= 5:

            # There is a 5% chance the random number will be under 5. If that happens, unicorn is token
            final_choice = "Unicorn"
            money += 5
        elif 6 <= computer_choice <= 35:

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

        # asking the user if they want to continue
        play_again = input(f"Hit enter if you want to continue to round {rounds + 1}? If you want to quit enter 'x': ")
    else:
        play_again = "x"

# Print the start balance and what the user ended with
print("---------------------------------------")
print(f"You starting balance was {STARTING_BALANCE:.2f} ")
print(f"You final balance is ${money:.2f}")
