"""
Getting out loops with break

Works the same way as C or Java

We use to leave loops in a forced (projected) way
"""


# Example 1
for number in range(1, 11):
    if number == 6:
        break
    else:
        print(number)
print("I left the for loop.")


# Example 2
while True:
    command = input("Type 'rescue' to rescue me from this loop: ")
    if command == 'rescue':
        break
print("Thanks!")
