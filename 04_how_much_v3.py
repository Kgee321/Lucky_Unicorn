"""Component 2 -- How much version 3
repeating the functions so I can efficiently test this code and screenshot it
Written by Katelyn Gee
05/04/2022"""


def number_checker(question, low, high):
    error = "Error, try again! Please enter a whole number between 1 and 10."

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
                print()

        except ValueError:
            # print error if not a valid integer
            print(error)
            print()


# calls on functions and prints how much money the user is using
for i in range(8):
    print(f"You are using ${number_checker('Enter the amount of money you want to play with between 1 and 10: $', 1, 10)}")
    print()
