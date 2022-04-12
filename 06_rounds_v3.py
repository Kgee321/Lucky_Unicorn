"""Component 4 -- Version 3
Converting version 2 into a functions
By Katelyn Gee
12/04/2022"""

# makes the random function accessible
import random


def looping_rounds(money):

    # starting variable for loop
    play_again = ""
    rounds = 0

    # function to generate a random token
    while play_again != "x":

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
        computer_choice = random.randint(1, 100)
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
        if money == 0:
            play_again = "x"
            print("Sorry, you ran out of money")
        else:
            # asking the user if they want to continue
            play_again = input(f"Hit enter if you want to continue to round {rounds + 1}? If you want to quit enter 'x': ")
    return money


# Starting cost
STARTING_BALANCE = 5

# Print the start balance and what the user ended with
final_balance = looping_rounds(STARTING_BALANCE)
print("---------------------------------------")
print("Thanks for playing!")
print(f"You starting balance was {STARTING_BALANCE:.2f} ")
print(f"You final balance is ${final_balance:.2f}")
print("Goodbye")
