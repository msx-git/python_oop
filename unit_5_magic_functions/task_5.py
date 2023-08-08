class Book:
    def __init__(self, title, category):
        self.title = title
        self.category = category

    def __str__(self):
        return f'Book - title:{self.title}, category:{self.category}'


class Library:
    def __init__(self):
        self.books = []

    def add(self, book):
        assert isinstance(book, Book), 'You can only add book'
        self.books.append(book)

    def __getitem__(self, item):
        return self.books[item]


b1 = Book('Python', 'Computer Science')
b2 = Book('Notebook', 'Novel')
b3 = Book('C++', 'Computer Science')
b4 = Book('Twilight', 'Novel')

lib = Library()
lib.add(b1)
lib.add(b2)
lib.add(b3)
lib.add(b4)

for book in lib:
    print(book)
