"""
OOP - Properties

In programming languages as Java, when declaring private attributes in classes, we use to create public methods to \
manipulate those attributes. This methods are known as getters and setters, where getters return the attribute value \
and setters alter the value.
"""


class CheckingAccount:
    """The CheckingAccount Class is encapsulating the attributes number, holder, limit and debit_limit."""
    __counter = 10000
    __transfer_fee = 10

    def __init__(self, holder, balance, limit):
        self.__number = CheckingAccount.__counter
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit
        self.__debit_limit = 300
        CheckingAccount.__counter += 1

    """We will now transform the attributes we want to make public into properties using the decorator @property."""

    @property
    def number(self):
        return self.__number

    @property
    def holder(self):
        return self.__holder

    @property
    def balance(self):
        return self.__balance

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, new_limit):
        self.__limit = new_limit

    """It is also possible to create methods as properties."""

    def show_balance(self):
        return f"The holder {self.__holder} balance is {self.__balance} with credit limit of {self.__limit}."

    def deposit(self, how_much):
        if how_much > 0:
            self.__balance += how_much
            return True
        else:
            print("You can't withdraw money within this option. Please use the withdraw(how_much) method.")
            return False

    def withdraw(self, how_much):
        if self.__balance - how_much < - self.__debit_limit:
            print(f"Sorry, you can't withdraw more than {self.__balance + self.__debit_limit} dollars.")
            return False
        elif how_much < 0:
            print("You can't deposit money within this option. Please use the deposit(how_much) method.")
            return False
        else:
            self.__balance -= how_much
            return True

    def transfer_money_to(self, destination, how_much):
        if self.withdraw(how_much + CheckingAccount.__transfer_fee):
            destination.deposit(how_much)

    @property
    def available_to_withdrawn(self):
        return self.__balance + self.__debit_limit

    # """The next six methods (getters and setters) is what is done in Java to get/set attributes."""
    # def get_number(self):
    #     return self.__number
    #
    # def get_holder(self):
    #     return self.__holder
    #
    # def get_balance(self):
    #     return self.__balance
    #
    # def get_limit(self):
    #     return self.__limit
    #
    # def set_balance(self, balance):
    #     self.__balance = balance
    #     return self.__balance
    #
    # def set_limit(self, limit):
    #     self.__limit = limit
    #     return self.__limit


account_1 = CheckingAccount('Felicity Jones', 3000, 5000)
account_2 = CheckingAccount('Angelina Julie', 2000, 4000)

print(account_1.show_balance())
print(account_2.show_balance())

print("""
The best say to obtain/manipulate attributes from the Class in Java is to create getter/setter methods inside it.
Suppose we want to get the summing of all balances in the bank: we must create a getter method inside the Class. 
""")
# print(sum(account.get_balance() for account in [account_1, account_2]))

print("""
When declaring the @property decorator in the Class methods, they become properties. We can access them without the \
parenthesis usually required for functions ().
""")
print("The summing of balances is: ", sum(account.balance for account in [account_1, account_2]))

print("Let's now change Felicity limit: ")
print(account_1.__dict__)
account_1.limit = 999999999999
print(account_1.__dict__)

[print(f"The total value available for {account.holder} to withdrawn is: {account.available_to_withdrawn}")
 for account in [account_1, account_2]]
