"""Editing 01_yes_no_v1. Adding .lower() to question,
so it does not matter if they enter capital letters or lowercase letters
checking if user input is lower case by printing it at the end
I put it into a basic function so when they user enters an incorrect input, it repeats
the functions until they input the correct input"""


def yes_no():
    # Ask user if they have played the game in the past
    question = input("Do you know how to play this game (Lucky Unicorn)? Y/N ").lower()

    # If yes, calling on game function
    if question == "y" or question == "yes":
        print("Program continues")
        # game()

    # If no, calling on instruction function
    elif question == "n" or question == "no":
        print("Display instructions")
        # instructions()

    # If incorrect input, repeat questions
    else:
        print("Incorrect input, please enter yes or no (y/n).")
        print()
        yes_no()
    print(f"You entered {question}")


yes_no()
