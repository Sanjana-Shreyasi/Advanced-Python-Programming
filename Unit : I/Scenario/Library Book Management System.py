#Unit 1 : Question 3
#Library Book Management System
class Book:
    def __init__(self, book_id, title, author, price):
        # storing basic details of a book
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def get_category(self):
        # deciding if book is premium or standard
        if self.price >= 500:
            return "premium"
        else:
            return "standard"

    def show(self):
        # printing all details of one book
        print("Book id:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Category:", self.get_category())


class Library:
    def __init__(self, name):
        self.name = name
        # list to store all books
        self.books = []

    def add_book(self, book):
        # adding one book to the list
        self.books.append(book)
        print(book.title, "added to library")

    def show_all(self):
        # showing every book one by one
        print("All books in", self.name)
        for b in self.books:
            b.show()
            print()


# creating library object
lib = Library("City Public Library")

# creating book objects
b1 = Book(1, "Python for beginners", "John Smith", 450)
b2 = Book(2, "Data science handbook", "Alice Brown", 850)
b3 = Book(3, "Short stories", "Mike Lee", 200)

# adding books to library
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

print()

# showing all books at the end
lib.show_all()

#Output
'''Python for beginners added to library
Data science handbook added to library
Short stories added to library

All books in City Public Library
Book id: 1
Title: Python for beginners
Author: John Smith
Price: 450
Category: standard

Book id: 2
Title: Data science handbook
Author: Alice Brown
Price: 850
Category: premium

Book id: 3
Title: Short stories
Author: Mike Lee
Price: 200
Category: standard'''