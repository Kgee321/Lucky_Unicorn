"""Converting it into a while loop so we can efficiently test if the code is working"""

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


yes_no()
