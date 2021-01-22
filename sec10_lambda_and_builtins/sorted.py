"""
Don't confuse with the function sort() we already study in lists. The sort() function works only with lists, while \
the sorted() function works with every iterable.

 - sorted() doesn't act on the argument as the sort() function does. However, it also returns a sorted list.
 - A custom key function can be supplied to customize the sort order, and the reverse flag can be set to request the \
 result in descending order.

sorted(iterable, /, *, key=None, reverse=False)
 - key: provide a function to sort the data.
 - *: this will unpack all extra parameters
 - /: this is an extra parameter which I don't know how to use
"""

# We can use sorted() for more complex tasks:
# Look at this tweets
users = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]
# the key parameter receives a function in which to sort the data
# this next list will be sorted by number of tweets for each user
print(sorted(users, key=lambda user: len(user.get('tweets')), reverse=True))



