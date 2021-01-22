"""
Filter

filter() -> filter data from a determined collection.
"""
import statistics  # library to work with statistics

# filtering above average:
numbers = [98, 54, 96, 21, 54, 57, 54, 87, 10, 99, 5, 45, 65, 85, 78, 31]
average = statistics.mean(numbers)
# as is the case for map() function, filter() also receives
# two parameters, one bool and one iterable
# the bool can be the output of a lambda function
above_average = filter(lambda x: x > average, numbers)
print(f"The grades above the average {average} are {list(above_average)}.")
print(above_average)
# after using the filter, it is discarded
print("Now the filter is deleted: ", list(above_average))

# o filter is also used for excluding missing data
countries = [' ', 'Brazil', 'Argentina', 'United States', 'Australia',
             'New Zealand', '', 'Venezuela']
countries_fixed = filter(None, countries)
countries_fixed = list(countries_fixed)
print(countries_fixed)

# option to remove white spaces
countries_fixed = filter(lambda country: len(country) > 2, countries)
countries_fixed = list(countries_fixed)
print(countries_fixed)

# Exemplo mais complexo

users = [
    {"username": "samuel", "tweets": ["Eu adodo bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]
print(users)

# Filtrar os usuários que estão inativos no Twitter
# first way (my way)
filter_inactive = filter(
    lambda user: len(user.get("tweets")) == 0
    # I could use not user.get("tweets") for conditional but it is ugly
    # and python should be beautiful.
    , users)
inactive_users = list(filter_inactive)
inactive_usernames = [inactive_user.get('username') for inactive_user in inactive_users]
print(f"The inactive users are: {inactive_usernames}")


# Combining filter and maps
# We should create a list containing "Your instructor is" + name,
# if each name have less than 5 characters
names = ['Vanessa', 'Ana', 'Maria']
filter_name = filter(lambda name: len(name) < 5, names)
filtered_names = list(filter_name)
map_instructors = map(lambda instr_name: f"Your instructor is {instr_name}", filtered_names)
messages = list(map_instructors)
print(messages)
# in one line:
messages = list(map(lambda instr: f'Sua instrutora é {instr}', filter(lambda name: len(name) < 5, names)))
print(messages)
