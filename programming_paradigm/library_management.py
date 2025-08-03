class Book:
    """
    Represents a book in the library system.
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        _is_checked_out (bool): True if the book is checked out, False otherwise.
                                 
    """
def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

def check_out(self):
        """Marks the book as checked out if it's currently available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True 
        return False 

def return_book(self):
        """Marks the book as available if it's currently checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True 
        return False 

def is_available(self):
        """Returns True if the book is available (not checked out), False otherwise."""
        return not self._is_checked_out

def __str__(self):
        """Returns a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}"

class Library:
    """
    Manages a collection of Book objects.
    Attributes:
        _books (list): A private list to store Book instances.
    """
    def __init__(self):
        self._books = [] # Private list to store Book objects

    def add_book(self, book):
        """Adds a Book object to the library's collection."""
        if isinstance(book, Book): # Optional: Ensure we're adding a Book object
            self._books.append(book)
            print(f"Added '{book.title}' to the library.")
        else:
            print("Error: Only Book objects can be added to the library.")

    def check_out_book(self, title):
        """
        Attempts to check out a book by its title.
        If found and available, marks it as checked out.
        """
        for book in self._books:
            if book.title == title:
                if book.check_out(): # Call the book's method to change its status
                    print(f"'{title}' has been checked out.")
                    return True
                else:
                    print(f"'{title}' is already checked out.")
                    return False
        print(f"Error: '{title}' not found in the library.")
        return False

    def return_book(self, title):
        """
        Attempts to return a book by its title.
        If found and checked out, marks it as available.
        """
        for book in self._books:
            if book.title == title:
                if book.return_book(): # Call the book's method to change its status
                    print(f"'{title}' has been returned.")
                    return True
                else:
                    print(f"'{title}' was not checked out.")
                    return False
        print(f"Error: '{title}' not found in the library.")
        return False

    def list_available_books(self):
        """Prints the title and author of all currently available books."""
        available_found = False
        for book in self._books:
            if book.is_available(): # Use the book's method to check availability
                print(book) # This will use the Book's __str__ method
                available_found = True
        if not available_found:
            print("No books currently available.")


