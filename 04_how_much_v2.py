"""Component 2 -- How much version 2
Editing version 1 -- making it more effective and more simple
Written by Katelyn Gee
31/03/2022"""


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


# calls on functions and prints how much money the user is using
print(f"You are using ${number_checker('Enter the amount of money you want to play with between 1 and 10: $', 1, 10)}")
