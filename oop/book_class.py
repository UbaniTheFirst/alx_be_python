class Book:
    def __init__(self, title, author, year):
        """Constructor: Initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """Destructor: Print deletion message when object is deleted."""
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """String representation: Return human-readable string."""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Official representation: Return string that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
