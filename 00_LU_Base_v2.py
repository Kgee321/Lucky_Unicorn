""" Based on base version 1.
Adding more components to it as they are created.
 Katelyn Gee
 12/04/2022"""

# importing random generator
import random


# yes/no checker function goes here:
def yes_no(asking):
    while True:
        # Ask user if they have played the game in the past
        question = input(asking).lower()

        # If yes, calling on game function
        if question == "y" or question == "yes":
            question = "Yes"
            return question

        # If no, calling on instruction function
        elif question == "n" or question == "no":
            question = "No"
            return question

        # If incorrect input, repeat questions
        else:
            print("Incorrect input, please enter yes or no (y/n).")
    return question


# function to display instructions
def instructions():
    print("*** How to play ***")
    print()
    print("The game rules will go here")
    print()
    print("Program continues")
    print()


# Number checking functions
def number_checker(question, low, high):
    error = "Error, try again! Please enter a whole number between 1 and 10."
    amount = 0

    # Keeps asking until the correct value is entered
    while True:
        try:
            # asking the question
            amount = int(input(question))
            print()

            # checking if the number is between the required amount
            if low <= amount <= high:
                return amount
            else:
                print(error)

        except ValueError:
            # print error if not a valid integer
            print(error)


# looping rounds function
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


# Yes/No checker main routine
played_before = yes_no("Do you know how to play this game (Lucky Unicorn)? Y/N ")

if played_before == "No":
    instructions()


# How much checker main routine
print()
user_balance = number_checker('Enter the amount of money you want to play with between 1 and 10: $', 1, 10)
print(f"You are using ${user_balance}")


# looping rounds main routine

# Print the start balance and what the user ended with
final_balance = looping_rounds(user_balance)
print("---------------------------------------")
print("Thanks for playing!")
print(f"You starting balance was {user_balance:.2f} ")
print(f"You final balance is ${final_balance:.2f}")
print("Goodbye")
