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


# Yes/No checker main routine
played_before = yes_no("Do you know how to play this game (Lucky Unicorn)? Y/N ")

if played_before == "No":
    instructions()


# How much checker main routine
print()
user_balance = number_checker('Enter the amount of money you want to play with between 1 and 10: $', 1, 10)
print(f"You are using ${user_balance}")

