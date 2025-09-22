class Book:
    def __init__(self, title, author):
        """Initialize a Book with title and author."""
        self.title = title
        self.author = author
    
    def __str__(self):
        """Return string representation of Book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an EBook with title, author, and file_size."""
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """Return string representation of EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook with title, author, and page_count."""
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """Return string representation of PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        """Initialize a Library with an empty list of books."""
        self.books = []
    
    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)
    
    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)
