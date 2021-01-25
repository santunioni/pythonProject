"""
OOP - Abstraction and Encapsulation

What is the difference of Object Oriented Programming. OOP doesn't open any magic door for programming, nor it add any \
resources not present in procedural programming. However the programming paradigms are different from each other in a \
way that choosing the right paradigm for your project may facilite your life a lot. But in principle the same things \
you can do with a specific paradigm, you can do with all others. OOP is unique in the way we think about hwo to solve \
the problem in our hands.

The Object Oriented Programming main objective is to encapsulate our code inside a logical and hierarchical group \
using classes.


The Class ENCAPSULATES the properties:

                Class
|---------------------------------|
|      attributes and method      |
|_________________________________|


______________________________________________________________________________________________________________________ |
 - Remembering: private attribute/methods in Python:
 Imagine we have a class called Person, encapsulating an private attribute called __name and a private method called \
 __speak()
 These private elements should only be accessed inside the class. However, Python doesn't block access outside the \
 class. A phenomena called Name Mangling happens, which alter the way we access private elements from outside the \
 class. We can therefore access them calling: instance._ClassName__element
-----------------------------------------------------------------------------------------------------------------------|


Abstraction, in Object Oriented Programming, is the act of exposing only relevant data from the class, hiding private \
methods and attributes from the user (the person calling the class by creating an object).
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

    def show_balance(self):
        print(f"The holder {self.__holder} balance is {self.__balance} with credit limit of {self.__limit}.")
        # return self.balance

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


bank_account_1 = CheckingAccount('Vinicius', 10000, 1000)
print(bank_account_1.show_balance())
print(bank_account_1._CheckingAccount__balance)
bank_account_1.withdraw(10300)
print(bank_account_1._CheckingAccount__balance)

print("""Even when the attributes are private we can access from outside the class: """, end="")
bank_account_1._CheckingAccount__balance = 10000000000
print(bank_account_1._CheckingAccount__balance, ". We can't fix it because it's a characteristic of Python language.")

bank_account_2 = CheckingAccount('Bianca', 0, 10)
print(bank_account_1.__dict__)
print(bank_account_2.__dict__)

print("""What if I want to transfer values from different accounts? """)
bank_account_1.transfer_money_to(bank_account_2, 10000000000*2)
print(bank_account_1.__dict__)
print(bank_account_2.__dict__)

print("""What if I want to transfer values from different accounts? """)
bank_account_1.transfer_money_to(destination=bank_account_2, how_much=10000000)
print(bank_account_1.__dict__)
print(bank_account_2.__dict__)
