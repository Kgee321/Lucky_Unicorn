"""Component 2 -- How much version 2
Editing version 1
Written by Katelyn Gee
31/03/2022"""


def number_checker(question):
    error = "Error, try again! Please enter a number between 1 and 10."
    valid = False

    # Keeps asking until the correct value is entered
    while not valid:
        try:
            # asking the question
            amount = int(input(question))
            if 1 <= amount <= 10:
                # breaks the loop if correct value
                valid = True
                return amount
            else:
                # prints error if not between 1 and 10
                print(error)
        except ValueError:
            # print error if not a valid integer
            print(error)


# calls on functions and prints how much money the user is using
print(f"You number is {number_checker('Enter the amount of money you want to play with between 1 and 10: $')}")
