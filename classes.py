class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

# an = PartyAnimal()
# print(type(an))
# print(dir(an))

class PartyAnimal2:
    x = 0
    def __init__(self):
        print('Im constructed')

    def party(self):
        self.x = self.x + 1
        print('so far', self.x)

    def __del__(self):
        print('Im deconstructed', self.x)

# an2 = PartyAnimal2()
# an.party()
# an.party()
# an = 42
# print('an contains', an)


class PartyAnimal3:
    x = 0
    name = ''
    def __init__(self, z):
        self.name = z
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x+1
        print(self.name, 'party count', self.x)

# s = PartyAnimal3('Sally')
# j = PartyAnimal3('Jim')
#
# s.party()
# j.party()
# s.party()

class Employee:
    def __init__(self, ID, first_name, surname, salary, department):
        self.ID = ID
        self.first_name = first_name
        self.surname = surname
        self.salary = salary
        self.department = department

    def showEmployeeDetails(self):
        print(f'ID = {self.ID}\n first_name = {self.first_name}\n surname = {self.surname}\n '
              f'salary = {self.salary}\n department = {self.department}')

    def calcNetSalary(self):
        if self.salary < 34800:
            get_30_percent = self.salary/100 * 30
            print(f'net salary = {self.salary - get_30_percent}')
        else:
            get_40_percent = self.salary / 100 * 40
            print(f'net salary = {self.salary  - get_40_percent}')

# mark = Employee(123, 'mark', 'zucerberg', 10000, department='backend')
# mark.showEmployeeDetails()
# mark.calcNetSalary()

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f'{self.name} makes sound {self.sound}')

#subclass
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 'Woof')

    def make_sound(self):
        print(self.name, 'makes sound: Woof!')

#subclass
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, 'Meow')

    def make_sound(self):
        print(self.name, 'makes sound Meow')

# generic_animal = Animal('Some Animal', '??')
# dog = Dog('Buddy')
# cat = Cat('huyasi')
#
# #base class sound
# generic_animal.make_sound()
# dog.make_sound()
# cat.make_sound()


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'{self.title} by {self.author}'

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'added {book}')

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f'removed book {book}')
                return
        print(f'Book title {title} not found')

    def display_books(self):
        if not self.books:
            print('Library is empty')
        else:
            print('books in the library:')
            for i in self.books:
                print(f' - {i}')

# library = Library()
#
# book1 = Book("1984", "George Orwell")
# book2 = Book("To Kill a Mockingbird", "Harper Lee")
# book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
#
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
#
# library.display_books()
#
# library.remove_book('1984')
# library.remove_book('Moby Dick')
#
# library.display_books()



































