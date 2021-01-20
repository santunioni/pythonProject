"""
String type

A variable is string type in Python always that:
 - Is between single quotes: `Single quote string`
 - Is between double quotes: "Double quote string"
 - Is between triple single quotes: '''Triple double quote string'''
"""
#- Is between triple double quotes: """Triple double quote string"""


single_quote = 'single_quote'
print(f'The variable {single_quote} is {type(single_quote)}')


double_quote = "double_quote"
print(f'The variable {double_quote} is {type(double_quote)}')


triple_single_quote = '''triple_single_quote'''
print(f'The variable {triple_single_quote} is {type(triple_single_quote)}')


triple_double_quote = """triple_double_quote"""
print(f'The variable {triple_double_quote} is {type(triple_double_quote)}')


location = "Gina's bar"
print(f'The variable {location} is {type(location)}')


now_I_am_breaking_line = '\n This first line comes before \n this second line \n'
print(f'The variable {now_I_am_breaking_line} is {type(now_I_am_breaking_line)}')


breaking_line_again = """This first line comes before
this second line"""
print(f'\n The variable {breaking_line_again} is {type(breaking_line_again)}')


print(f'\n Now I am yelling: \n {breaking_line_again.upper()}')


print(f'\n Now I am speaking low: \n {breaking_line_again.lower()}')


def phrase_to_list(phrase_string):
    return phrase_string.split()


phrase_string = "Hello. My name is Goku!"
phrase_list = phrase_to_list(phrase_string)
print(f"The variable {phrase_string} is type {type(phrase_string)}")
print(f"The variable {phrase_list} is type {type(phrase_list)}")


# This is called STRING SLICING
number_of_char = 35
print(f"Now am an taking only the first {number_of_char} from the variable now_I_am_breaking_line")
print(now_I_am_breaking_line[1:number_of_char+1])


def invert(string):
    """I can invert the string"""
    # start from the first, go to the last and invert!
    return string[::-1]


print(invert(phrase_string))


def reading_in_numbers(string):
    """I can replace characters in the string"""
    string = string.upper()
    string = string.replace('E', '3')
    string = string.replace('A', '4')
    string = string.replace('O', '0')
    string = string.replace('S', '5')
    string = string.replace('L', '1')
    string = string.replace('I', '!')
    string = string.replace('T', '7')
    return string


# I can search for letters!
where_is_Goku = "Oi. Eu sou o Goku!".index("Goku")


# String concatenation
name = "Vinicius" + " Vargas "
name = name*3
print(name)


# We can also print EMOJIS:
# access https://apps.timwhitlock.info/emoji/tables/unicode
# Original: U+1F60D
# Modified: U0001F60D
emoji = '\U0001F60D'
print(emoji)
