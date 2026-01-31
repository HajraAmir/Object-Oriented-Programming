class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def __str__(self):
        return f"Author: {self.name}, Nationality: {self.nationality}"

class Publisher:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Publisher: {self.name}, Address: {self.address}"

class Book:
    def __init__(self, title, author, publisher, price):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.price = price

    def book_info(self):
        return f"Book: {self.title}\n{self.author}\n{self.publisher}\nPrice: ${self.price:.2f}"

# Creating instances of Author and Publisher
author = Author("George Orwell", "British")
publisher = Publisher("Secker & Warburg", "London")

# Creating an instance of Book using composition
book = Book("1984", author, publisher, 15.99)

# Displaying book information
print(book.book_info())