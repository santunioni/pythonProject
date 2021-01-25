"""
We already known what objects are. We used objects in all previously classes in this sections. Objects are\
 initializations (instances) of the classes, after providing the class the parameter a specific object will possess.
"""
from methods import User, Lamp

print("\n\n\n\n")
lamp1 = Lamp('white', 110, 60)
print(f"""Is lamp1 on? {lamp1.is_on()}. Ok, so we will turn it {"off" if not lamp1.switch() else "on"} for you now.\
 Is the lamp on now? {lamp1.is_on()}.""")

print("Objects can be passed as parameter to other classes.")
user_vinicius = User('Vinícius', 'Vargas', 'asdfg.sadgd@ufv.br', '123456')
class CheckingAccount:
    # This is a Class attribute, shared among all instances for the Class.
    counter_to_identify = 4999  # This is a Class attribute useful to register products id

    # In other languages as Java, the class attributes are called static attributes.

    def __init__(self, limit, balance, client):
        self.__number = CheckingAccount.counter_to_identify + 1
        self.__limit = limit
        self.__balance = balance
        self.__client = client

    """The following two blocks demonstrates the right way to recover private attributes form the class. We should \
    create functions that return the attributes."""

    def show_limit(self):
        return self.__limit

    def show_balance(self):
        return self.__balance

    def client_name(self):
        return self.__client.full_name()


account = CheckingAccount(5000, 1000, user_vinicius)
