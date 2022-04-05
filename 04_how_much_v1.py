"""Component 2 -- How much version 1
Asker the user how much they want to spend and they can only enter a number between 1 and 10.
If it is higher 10 or lower 1 or a string, it will enter an invalid message and repeat the question.
Written by Katelyn Gee
31/03/2022"""


def number_checker():
    error = "Error, try again! Please enter a number between 1 and 10."
    valid = False
    while not valid:
        try:
            amount = int(input('Enter a number between 1 and 10: '))
            if 1 <= amount <= 10:
                valid = True
                return amount
            else:
                print(error)
        except ValueError:
            print(error)


print(f"You number is {number_checker()}")
