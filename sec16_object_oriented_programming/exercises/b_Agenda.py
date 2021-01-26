from sec16_object_oriented_programming.exercises.a_Person import Person


class PersonBook:

    def __init__(self, capacity, initial_list=[]):
        self.__person_book = initial_list
        self.__capacity = capacity

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, new_capacity):
        if new_capacity >= len(self.__person_book):
            self.__capacity = new_capacity
        else:
            raise IndexError("You can't set capacity below the number of contacts.")

    def add_to_book(self, new_person):
        if len(self.__person_book) < self.__capacity:
            self.__person_book.append(new_person)
        print(f"The PersonBook has reached maximum capacity.")

    def remove_from_book(self, person_to_rm):
        if person_to_rm in self.__person_book:
            self.__person_book.remove(person_to_rm)
        else:
            print(f"This book doesn't not have this contact.")

    def index_to_person(self, index):
        if index < len(self.__person_book):
            return self.__person_book[index]
        else:
            print("Index out of person list.")

    def person_data(self, index):
        person = self.index_to_person(index)
        return {'index': index, 'name': person.name, 'age': person.age, 'height': person.height}

    def print_book(self):
        return [self.person_data(index) for index in range(len(self.__person_book))]


myself = Person('Vinicius Vargas', 25, 1.78)
bibi = Person('Bianca Lugatti', 23, 1.71)

agenda = PersonBook(capacity=10, initial_list=[myself, bibi])
print(agenda.person_data(1))

pedro = Person('Pedro Dardengo', 24, 1.77)
mae = Person('Aparecida Angelo', 56, 1.65)

agenda.add_to_book(mae)
agenda.add_to_book(pedro)
agenda.capacity = 4

print(agenda.print_book())

agenda.remove_from_book(mae)
agenda.capacity = 3

print(agenda.print_book())
