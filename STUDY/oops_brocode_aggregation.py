#Aggregation- Represents a relationship where one class has a reference to another class. It is a "has-a" relationship, but the contained object can exist independently of the container object.

class Library:
    def __init__(self, name):
         self.name = name
         self.books = []  # Starts with an empty book list
         
    # Add an existing book to the library
    def add_book(self, book):
        self.books.append(book)      
        
    # List all books in the library
    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]
    
# Book class represents an independent book object
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author 

# Create a Library object
library = Library("New York Public Library")

# Create Book objects independently (not tied to the library yet)
book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J. R. R. Tolkein")
book3 = Book("The Colour of Magic", "Terry Pratchet")

# Add books into the library (aggregation: library uses existing books)
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display the library name
print(library.name)

# Display all books in the library
for book in library.list_books():
    print(book) 