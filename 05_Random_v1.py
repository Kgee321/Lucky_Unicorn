"""Component 3 -- Version 1
Generates a random token in random order
By Katelyn Gee
07/04/2022"""

# makes the random function accessible
import random

# list of animals for computer to randomly choose
animals = ["Zebra", "Unicorn", "Horse", "Donkey"]

# computer chooses a random animal 20 times and printing it
for i in range(20):
    computer_choice = random.choice(animals)
    # print computer choice
    print(computer_choice, end='\t')

