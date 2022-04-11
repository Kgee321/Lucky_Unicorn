""" Component 4 -- Version 1 -- Looping rounds
Set to $5 in the user balance
Only using the donkey token to start off
Written by Katelyn Gee
11/04/2022  
"""
# The round it is
rounds = 1
money = 5
while money != 0:
    print(f"Round {rounds}")
    print()
    playing = input("Press enter to play round {rounds} or X to exit the game: ").lower()
    print()
    if playing == "":
        print("Round continues")
        print()
        rounds += 1
        money -= 1
    elif playing == "x":
        print(f"Goodbye! Your balance is ${money}")
        print()
    else:
        print("Incorrect input, please either hit enter to continue or enter 'x'.")
        print()



