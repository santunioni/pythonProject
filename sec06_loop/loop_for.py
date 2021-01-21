"""
Loop for

Loop -> repetition structure
For -> one of those structures


In C or Java we have:

for(int i = 0; i < 10; i++){
    //execution
}

In Python we have comprehension:

for _item in item:
    //execution
"""


# We use loops to iterate over sequences or iterable objects
string = "I am an iterable object"
for _char in string:
    print(_char)


my_list = [1, 2, 1, 254, 1, 23, 12, 4, 12, 4]
numbers = range(1, 10)
# numbers_inverted = n


# Iteration over lists
for _my_number in zip(numbers, numbers.__reversed__()):
    print(_my_number)


# the enumerate function turns a iterable object into
# an tuple whose elements are a pair with the _index
# and the value
for _index, _value in enumerate(string):
    print(_index, _value)


# the pythonic way
for _value in string:
    print(_value)


# to disregard one value
for _, _value in enumerate(string):
    print(_value)


self_reinforcements_amount = int(
    input("How many times do I have \
to tell you are awesome? "))
for _dummy in range(self_reinforcements_amount):
    print(f"You are awesome! {_dummy}")


# if you don't want to break lines
for _char in string:
    print(_char, end="")
print("")


# Let's do a tree with emojis: https://apps.timwhitlock.info/emoji/tables/unicode
def construct_pine_tree(
        _floor_number=3,
        _floor_height=10):

    _top_height = (_floor_height*3)//2
    _max_width = _top_height*2 + 1

    import random as rd

    def random_emoji():
        u_number = rd.choice(range(1, 40))
        _emoji = '\U0001F6{}'.format(u_number)
        return _emoji  # str(rd.choice(range(10)))

    def construct_top():
        for _i in range(_top_height):
            _emoji = random_emoji()
            print(" "*(_top_height - _i) + _emoji*(2*_i+1) + " "*(_top_height - _i))

    def construct_floor():
        to_print = ""

        _emoji = random_emoji()
        to_print += _emoji*_max_width

        for _i in range(1, _floor_height):
            _emoji = random_emoji()
            to_print_temp = '\n' + " "*_i + _emoji*(_max_width-2*_i) + " "*_i
            to_print += to_print_temp

        print(to_print[::-1])

    def construct_base():
        for _i in range(_floor_height):
            _emoji = random_emoji()
            print(" "*(_max_width//3) + _emoji*(_max_width//3+1) + " "*(_max_width//3))

    construct_top()
    for _f in range(_floor_number):
        construct_floor()
    construct_base()

    return None
