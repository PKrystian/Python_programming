class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.book_list = []
    
    def add_book(self, book):
        self.book_list.append(book)
        book.add_book(self.name)

    def rem_book(self, book):
        self.book_list.remove(book)
        book.rem_book()

    def show_all_books(self):
        for x in self.book_list:
            print(f"{x} is in {self.name} library")

class Book:
    def __init__(self, book, author, release_date) -> None:
        self.book = book
        self.author = author
        self.release_date = release_date
        self.library = None
    
    def add_book(self, library):
        self.library = library
        print(f"Book: {self.book} was added to: {self.library} library")

    def rem_book(self):
        self.library = None
        print(f"Book: {self.book} was removed from library")

    def __str__(self):
        return f"{self.book} {self.author} {self.release_date}"

lib1 = Library("ABC_library")
lib2 = Library("XYZ_library")
b1 = Book("Hobbit", "Tolkien", 1970)
b2 = Book("Punpun", "Asano", 2001)
b3 = Book("Berserk", "Miura", 1997)
b4 = Book("One piece", "Oda", 1997)
lib1.add_book(b1)
lib1.add_book(b2)
lib1.add_book(b3)
lib2.add_book(b4)
lib1.show_all_books()
lib1.rem_book(b1)
lib1.show_all_books()
lib2.show_all_books()