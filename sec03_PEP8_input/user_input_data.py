"""
Receiving user data
"""

# Entrada de dados
print("What is your name?")
nome = input()

age = int(input("What is your age? "))


# Print
print("Welcome, {}!".format(nome.title()))
am_I_correct = input(f"You were born in {2020-age}, right? (y/n) ")


# Processing
am_I_correct = am_I_correct[0].lower()


# Printing
if am_I_correct == 'y':
    print("Great!")
elif am_I_correct == 'n':
    print("Sorry. I am dumb.")
else:
    print("You are dumb!")
