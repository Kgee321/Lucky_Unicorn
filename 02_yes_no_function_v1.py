"""Putting the code into an efficient function so it is able to be used for any different
questions that involves a yes/no answer.
My storing the question  out of the function so different question can be asked and answered with this code another time.
Written by Katelyn Gee
28/03/2022"""


def yes_no(question):
    while True:
        # Ask user if they have played the game in the past
        question = input(question).lower()

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


# main function
show_instructions = yes_no("Do you know how to play this game (Lucky Unicorn)? Y/N ")
print(f"You entered {show_instructions}")



