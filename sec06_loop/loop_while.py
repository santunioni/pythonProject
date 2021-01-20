"""
Loop while


# ##########
# C or Java
# ##########
while(bool_value) {
    // run
}
OR
do {
    // run
}while(bool_value);
"""


bool_value = False
while bool_value:
    # Execute
    print("Hello!")

# it is very important to take care the stop criteria
# to not enter infinite loop


answer = ''
while answer != 'yes':
    answer = input('Have you finished your work, Bianca? ')
    answer = answer.lower()
print("Good job!")


