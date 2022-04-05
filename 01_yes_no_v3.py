""" Taking out the function and using a while loop.
This is so I can efficiently test my code to make sure it is working,
and it is easy to screenshot it all at once.
"""

question = ""
while question != "x":
    # Ask user if they have played the game in the past
    question = input("Do you know how to play this game (Lucky Unicorn)? Y/N ").lower()

    # If yes, calling on game function
    if question == "y" or question == "yes":
        print("Program continues")
        # game()

    # If no, calling on instruction function
    elif question == "n" or question == "no":
        print("Instructions displayed")
        # instructions()

    # If incorrect input, repeat questions
    else:
        print("Incorrect input, please enter yes or no (y/n).")
    print(f"You entered {question}")
    print()


