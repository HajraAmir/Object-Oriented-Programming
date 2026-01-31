class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def list_books(self):
        for book in self.books:
            print(book)

# Example usage
book1 = Book("1984", "George Orwell")
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald")

lib = Library("Central Library")
lib.add_book(book1)
lib.add_book(book2)

print(f"Books available in {lib.name}:")
lib.list_books()

# Removing a book
lib.remove_book(book1)
print(f"\nBooks available in {lib.name} after removing one book:")
lib.list_books()
