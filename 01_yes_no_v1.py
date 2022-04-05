"""Yes or no code -- Asks the user if they have played the game before.
If they have, outputs Program continues
If they have not, outputs display instruction
"""

# Ask user if they have played the game in the past
question = input("Do you know how to play this game (Lucky Unicorn)? Y/N ")

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



