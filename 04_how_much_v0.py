"""Component 2 -- How much version 0 -- beginning verison
Asker the user how much they want to spend and they can only enter a number between 1 and 10.
If it is higher 10 or lower 1 or a string or a float, it will enter an invalid message and repeat the question.
It can only be used once
Written by Katelyn Gee
5/04/2022"""

error = "Error, try again! Please enter a number between 1 and 10."
valid = False
while not valid:
    try:
        amount = int(input('Enter a number between 1 and 10: '))
        if 1 <= amount <= 10:
            valid = True
            print(f"You number is {amount}")
    except ValueError:
        print(error)


