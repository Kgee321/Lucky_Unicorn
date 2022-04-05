""" create an instruction function for when the user does not know how to play,
 connecting codes
 Katelyn Gee
 05/04/2022"""


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


# main routine goes here:
played_before = yes_no("Do you know how to play this game (Lucky Unicorn)? Y/N ")

if played_before == "No":
    instructions()
else:
    print("Program continues")

