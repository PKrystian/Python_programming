class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.book_list = []
    def __str__(self) -> str:
        return f"{self.name}"
    def add_book(self, book):
        if book not in self.book_list:
            if book.is_added == False or book.library == self.name:
                self.book_list.append(book)
                book.add_library(self)
    def rem_book(self, book):
        if book in self.book_list:
            self.book_list.remove(book)
            book.rem_library(self)
    def show_all(self):
        return [str(book) for book in self.book_list]

class Book:
    def __init__(self, name, author) -> None:
        self.name = name
        self.author = author
        self.library = None
        self.is_added = False
    def __str__(self) -> str:
        return f"{self.name}, author: {self.author}"
    def add_library(self, library_name):
        if self.is_added == False:
            self.is_added = True
            self.library = library_name
            library_name.add_book(self)
    def rem_library(self, library_name):
        if self.is_added == True:
            self.is_added = False
            library_name.rem_book(self)
            self.library = None

b1 = Book("Pan Tadeusz","Mickiewicz")
b2 = Book("Lalka","Prus")
b3 = Book("To","King")

lib = Library("ABC Library")
lib2 = Library("XYC Library")


lib.add_book(b1)
lib.add_book(b2)

print(lib.show_all())

lib2.add_book(b1)

print(lib.show_all())
print(lib2.show_all())