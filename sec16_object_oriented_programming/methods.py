"""
OOP - Methods

 - Methods (functions) -> methods model the object behavior. This means the actions the object can perform in the\
 system are described by the methods.

In Python, as is the case for attributes, we divide the methods em 2 groups: The class methods and the instance\
 methods.

Instance methods: this are methods that can be called only from objects created within the class model. The class\
 itself can use this methods. For example: user = User(...). The code user.method() works, but User.method() won't.\
 However, you can also access the method for user with the code User(user, ) because the meethods always receive the\
 parameter self.

 - The dunder init method (__init__) is a special method called builder. It's function is to construct objects from the\
 class.

OBS: Every element in Python preceded and ended with duple underline is called dunder (double underline).
OBS: The dunder methods/functions in Python are called magic methods.
ATTENTION: Although we are not forbidden from using dunder while naming our methods, it is not advisable. This can\
conflict with python internal methods if the name you choose is a reserved method.

Class methods: They are not tied to any instance of the class, but only to the class itself. We use decorators to\
 designate class methods. In order languages the class methods are known as static methods.

Static methods: The python static method is different from the class method. It uses the decorator @staticmethod\
 instead of the @classmethod. The static method is static, can't change never. Because of it, it don't receive any\
  parameter as input.
"""


class Lamp:
    """This next block is the builder method. We declare the instances inside the builder method. The attributes are \
    private, defined only inside the class.

    The self argument means the method is receiving the own object as parameter. The word self is not mandatory, \
    however the first argument also refers to the object. Using the word self is a convention."""

    def __init__(self, voltage, color, luminosity):
        self.__voltage = voltage
        self.__color = color
        self.__luminosity = luminosity
        self.__turned_on = False

    def is_on(self):
        return self.__turned_on

    def switch(self):
        self.__turned_on = not self.__turned_on
        return self.__turned_on

#     # To make the attributes public we use the decorator @property and create
#     # methods that will return the private attributes of the class.
#     @property
#     def voltage(self):
#         return self.__voltage
#
#     @property
#     def color(self):
#         return self.__color
#
#     @property
#     def turned_on(self):
#         return self.__turned_on


class CheckingAccount:
    # This is a Class attribute, shared among all instances for the Class.
    counter_to_identify = 4999  # This is a Class attribute useful to register products id

    # In other languages as Java, the class attributes are called static attributes.

    def __init__(self, limit, balance):
        self.__number = CheckingAccount.counter_to_identify + 1
        self.__limit = limit
        self.__balance = balance

    """The following two blocks demonstrates the right way to recover private attributes form the class. We should \
    create functions that return the attributes."""

    def show_limit(self):
        return self.__limit

    def show_balance(self):
        return self.__balance


class Product:
    # This is a Class attribute, shared among all instances for the Class.
    theft = 0.35  # Very high consumption tax from Brazil
    counter_to_identify = 0  # This is a Class attribute useful to register products id

    # In other languages as Java, the class attributes are called static attributes.

    def __init__(self, name, description, price):
        self.__id = Product.counter_to_identify + 1
        self.__name = name
        self.__description = description
        self.__price = price * (1 + Product.theft)
        Product.counter_to_identify += 1

    def discount(self, percentage=0):
        """This method return a discount for the product, given a percentage. This is an instance method, created only\
        when called for a particular instance/object."""
        return self.__price * (1 - percentage / 100)


from passlib.hash import pbkdf2_sha256 as cryp


class User:
    counter = 0

    @classmethod
    def user_count(cls):
        """\
        This is a class method. The cls parameter (which is named this way by convention) receives the own class.\
         This method is accessible with the User.user_count command.

        The decorator @classmethod does the job of defining the class method for the class, not for the\
         instances/objects. The decorator always forces the own class to enter as parameter to the class method.\
         """
        return f'We have {cls.counter} users in the system.'

    @staticmethod
    def define():
        """The static method don't receive any parameter as input. For consequence it's is used mainly things that will\
        never change. This method is the same for all instances/objects."""
        return 'UXR344'

    def __init__(self, name, last_name, email, password):
        self.__id = User.counter + 1
        self.__name = name
        self.__last_name = last_name
        self.__email = email
        self.__password = cryp.hash(password, rounds=200000, salt_size=16)
        User.counter += self.__id
        print(f'New user created: {self.__gen_user()}')

    def run(self, meters):
        """This is an instance method. This means we can only use it after define an instance/object and calling the\
         method on it."""
        print(f'{self.__name__} is running {meters} meters.')

    def __run__(self, meters):
        """It is not recommended for us, developers, create dunder methods. Ths dunder methods are reserved for the\
         python methods by convention from the community."""
        print(f'{self.__name__} is running {meters} meters.')

    def full_name(self):
        return self.__name + ' ' + self.__last_name

    def check_pass(self, password):
        return cryp.verify(password, self.__password)

    def __gen_user(self):
        """This is a private method since we are initializing the name with __. However, the dunder is only a\
         convention. We can still access the method with user._User__gen_user()."""
        return self.__email.split('@')[0]


print("""\n
We can define a product and search it's price when applied a discount:
""")
rice = Product('Rice', 'Grain food widely consumed by brazilians', 15.00)
beans = Product('Beans', 'Grain food widely consumed by brazilians', 6.00)
discount_percentage = 50
print(f"The rice price with discount of {discount_percentage}% is: {rice.discount(discount_percentage)}.")

print(f"""What about this value? {Product.discount(beans, discount_percentage)}. In this case the product beans is\
 going to method discount() as the self parameter.""")

user = User('Vinicius', 'Vargas', 'vinicius.vargas@ufv.br', '1515432')
print("\nWe can access the user full name both ways: ")
print(user.full_name())
print(user.full_name() == User.full_name(user))

print(f"\nOne thing that isn't good about our code: we can access users password:")
print(f"This is user {user._User__name} password: {user._User__password}")
print("We will refactor the class in order to include cryptography.")

# name_user = input("Please inform your first name: ")
# last_name_user = input("Please inform your last name: ")
# email_user = input('Please inform your email: ')
# pass1_user = input('Please inform your password: ')
# pass2_user = input('Please confirm your password: ')
name_user = "Vinícius"
last_name_user = "Vargas"
email_user = "vinicius.vargas@ufv.br"
pass1_user = "12345"
pass2_user = "12345"
while pass1_user != pass2_user:
    print("Your password don't match with confirmation. Please type your password again.")
    pass1_user = input('Please inform your password: ')
    pass2_user = input('Please confirm your password: ')
user = User(name_user, last_name_user, email_user, pass1_user)
del name_user, last_name_user, email_user, pass1_user, pass2_user
# access_pass = input('Inform your password to gain access: ')
access_pass = "12345"
if user.check_pass(access_pass):
    print("Access granted.")
else:
    print("Access denied.")

print("""\n
We will now see how to call Class Methods. We don't have to create instances/objects for this task:
""")
# The correct way
print("The user counter is now: ", User.user_count())
# The wrong way because it's not necessary to create an user in order to call this method.
print("The user counter is now: ", user.user_count())


print("""All the methods created so far are Public methods. By convention wew create private methods preceding the\
 method name with dunder __
 Let's refactor the class User. We added the private method __gen_user() to the class.
 Let's try to access this method from the class:\
 """, end=" ")
try:
    print(user._User__gen_user())
    # print(user.__gen_user())
except AttributeError as err:
    print(f"You can't access a private method from the class. The following error as raised: {err}")
