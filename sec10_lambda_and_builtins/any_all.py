"""
Any and All
"""

print(
    """
all() -> returns True if all elements from an iterable are True or if the iterable is empty.
""")
# Example:
# False will be printed because bool(0) is False, not True.
print(all([0, 1, 2, 3, 4]))
# in the following case, True will be printed
print(all([1, 2, 3, 4]))

# Checking names initials
names = ['Carlos', 'ChowChow', 'Case', 'Cotista', 'Cuidado', 'caqui']
all_initials_are_C = all([name[0].upper() == 'C' for name in names])
if all_initials_are_C:
    print('\nAll names start with C.')
else:
    print("\nSomeone's name doesn't start with C.")

# We can check for vowels
vowels = 'aeiou'
russian_name = "jjjklllsdffghnmmnvccvbb"
print("\nAny vowels in the Russian name? ",
      not all([(letter not in vowels) for letter in russian_name])
      # the all() statement returns True if the name have only consonants, so we deny it to check for vowels
      # this task is easier with the any() function.
      )


print(
    """
any() -> returns True if any element from an iterable is True. Empty iterables return False.
""")
# Example:
# In the following print, True will be printed because bool(1) is True
print(any([0, 0, 0, 1, 2]))
# In the following print, False will be printed because bool(0) is False
print(any([0, 0, 0, 0, 0]))

# We can check for vowels
vowels = 'aeiou'
russian_name = "jjjklllsdffghnmmnvccvbb"
print("\nAny vowels in the Russian name? ",
      any([(letter in vowels) for letter in russian_name])
      # the any() statements returns True if he finds any vowel in the russian name
      )


print(
    """
The iterable Boolean argument can be a map() from a lambda function
""")
