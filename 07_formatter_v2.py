""" Component 5 -- Version 2
Testing my code for my evidence doc
Katelyn Gee
12/04/2022"""


# formatting main functions
def formatting(symbol, sentence):
    sides = symbol * 3
    sentence_style = f"{sides} {sentence} {sides}"
    symbol_style = symbol * len(sentence_style)
    return f"{symbol_style}\n{sentence_style}\n{symbol_style}"


# formatting main routines
print(formatting("!", "Congratulations, you got a unicorn"))
print()
print(formatting("-", "Welcome to Lucky Unicorn Game"))
print()
print(formatting("*", "Goodbye"))
