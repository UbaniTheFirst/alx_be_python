class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        """Initialize a book with title and author."""
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        """Check out the book."""
        self._is_checked_out = True
    
    def return_book(self):
        """Return the book."""
        self._is_checked_out = False
    
    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """A class representing a library that manages books."""
    
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []
    
    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
    
    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
    
    def list_available_books(self):
        """List all available books."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
