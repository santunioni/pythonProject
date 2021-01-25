"""
OOP - Attributes

Attributes -> represent the characteristics of the object wee are creating. With attributes we can represent the \
computationally the object status.

In Python, we split the attributes in 3 groups:
    - Instance attributes
    - Class attributes
    - Dynamics attributes

Instance attributes: are attributes declared inside the constructor method.


OBS: Builder method is a special method used to construct objects from classes.

In Java, a class Lamp, with attributes included, would be:
public class Lamp(){
    // declaring attributes
    protected float voltage;
    public String color;
    private Boolean turned_on = false;

    // declaring the constructor
    public Lamp(float voltage, String color){
        this.voltage = voltage;
        this.color = color;
    }

    // The next 3 blocks will public methods representing the private
    // attributes of the class. The public methods can be accessed by code.
    public float getVoltage(){
            return this.voltage;
    }
    public float getColor(){
            return this.color;
    }
    public float getTurned_on(){
            return this.turned_on;
    }
}

In Python the same class Lamp is defined as:
"""


class Lamp:
    """This next block is the builder method. We declare the instances inside the builder method. The attributes are \
    private, defined only inside the class.

    The self argument means the method is receiving the own object as parameter. The word self is not mandatory, \
    however the first argument also refers to the object. Using the word self is a convention."""

    def __init__(self, voltage, color):
        """The attributes are receiving the function arguments. When defined inside the builder method, they are \
        public by default. Public attributes can be accessed anywhere in the project.

        In case we want to make attributes private, which can only be accessed inside the own Class, we use Dunders \
        (double underscores __, also known as Name Mangling) before the attribute name when defining it.

        The following example defines public attributes:"""
        self.voltage = voltage
        self.color = color
        self.turned_on = False


class CheckingAccount:

    def __init__(self, number, limit, balance):
        """Remember: private attributes is only a convention. The Python language won't stop us from accessing the \
        private attributes outside the class. Suppose we create an object named my_bank_account with this class. \
        When calling a private attribute outside the class with my_bank_account.__balance (the balance attribute was \
        chosen to exemplify), python will exhibit an error message saying we shouldn't access the attribute this way. \
        However, we can still access the private attribute typing: my_bank_account__CheckingAccount__balance.

        The following example defines limit and balance attributes as private:"""
        self.number = number
        self.__limit = limit
        self.__balance = balance

    """The following two blocks demonstrates the right way to recover private attributes form the class. We should \
    create functions that return the attributes."""

    def show_limit(self):
        return self.__limit

    def show_balance(self):
        return self.__balance


print("""\n\nExample of accessing the private class attributes outside the class: """)
my_bank_account = CheckingAccount('71334-1', 2000.0, 100000.0)
print(f"My checking account number is {my_bank_account.number}")
print(f"My checking account balance is {my_bank_account._CheckingAccount__balance}")
# We have access, but if we define a private variable, we shouldn't access it this way. This is called name mangling.
# The attribute is still public, however it's name was mangled with the Class name.
print(f"The right way to show my_bank_account private balance is this: {my_bank_account.show_balance()}")


print("""\n\nThe following two classes are other examples for mapping real world entities into Classes in python.""")


class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


print("""\n\nWhat does instance/object attributes mean? It means that every instance/object created from the class will\
 have the same attributes, with it's particular values. Example:""")
bedroom_lamp = Lamp(110, 'yellow')
print(f"The instance/object bedroom_lamp have attributes voltage = {bedroom_lamp.voltage} and\
 color = {bedroom_lamp.color}. Each instance have it's own instance attributes.")


print("""What does Class attribute mean? Class attributes are attributes declared in the class directly, outside the\
 builder method. Generally we already assign a value to the attribute when defining it in the class. This value is\
 shared between all instances of this class, contrary to particular instance attributes.

Example: in the next class below, called Product, the attribute theft (representing taxes) is the same for all\
 instances for this class.""")


class Product:

    # This is a Class attribute, shared among all instances for the Class.
    theft = 0.35  # Very high consumption tax from Brazil
    counter_to_identify = 0  # This is a Class attribute useful to register products id
    # In other languages as Java, the class attributes are called static attributes.

    def __init__(self, name, description, price):
        self.id = Product.counter_to_identify + 1
        self.name = name
        self.description = description
        self.price = price*(1+Product.theft)
        Product.counter_to_identify += 1


rice = Product('Rice', 'Grain food widely consumed by brazilians', 15.00)
beans = Product('Beans', 'Grain food widely consumed by brazilians', 6.00)
# OBS: we don't need to create a class in order to have access to a class attribute
print(f"\nAfter taxation of {str(round(100*Product.theft))}% from the mafia, the rice and beans price are respectively\
 R${round(rice.price, 2)} and R${round(beans.price, 2)}.")
print(f"The rice id is {rice.id} and the beans id is {beans.id}.")


print("""\n
Now we will talk about dynamic attributes. This are attributes that may be created while the code is being executed.\
 This attribute will be exclusive of the instance/product that created it. You may learn how to create it, however\
 you must know it's is not common to use this type of attributes.

For example, a rice shortage:
""")
rice.stock = 0
print(f"""The rice stock is {rice.stock}.""")
# the next line break the code because beans don't have the stock attribute
# print(beans.stock)


print("""We can also dynamically delete attributes in the same way we've created them:""")
del rice.stock, rice.price
print("The code object.__dict__ returns the product transformed to a dictionary. Example:")
print(rice.__dict__)
