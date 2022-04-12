""" Component 5 -- Version 1
Allows user to enter a sentence and symbol and styles the page using those inputs
In a functions so any symbol or sentence can be used in the future
Katelyn Gee
12/04/2022"""


# formatting main functions
def formatting(symbol, sentence):
    symbol_style = symbol * len(sentence)
    sides = symbol * 3
    return f"{symbol_style}\n{sides} {sentence} {sides}\n{symbol_style}"


# formatting main routine
my_symbol = input("Enter a symbol: ")
my_sentence = input("Enter a sentence: ")
print(formatting(my_symbol, my_sentence))
