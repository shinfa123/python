# Base class Publisher
class Publisher:
    def __init__(self, publisher_id, publisher_name):
        self.publisher_id = publisher_id
        self.publisher_name = publisher_name
    
    # Method to display publisher details
    def display_publisher(self):
        return f"Publisher ID: {self.publisher_id}\nPublisher Name: {self.publisher_name}"

# Derived class Book from Publisher
class Book(Publisher):
    def __init__(self, publisher_id, publisher_name, title, author):
        # Invoke the constructor of the base class (Publisher)
        super().__init__(publisher_id, publisher_name)
        self.title = title
        self.author = author
    
    # Method to display book details, overriding the base class display method
    def display_book(self):
        return f"Title: {self.title}\nAuthor: {self.author}"

# Derived class Python from Book
class Python(Book):
    def __init__(self, publisher_id, publisher_name, title, author, price, no_of_pages):
        # Invoke the constructor of the base class (Book)
        super().__init__(publisher_id, publisher_name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages
    
    # Method to display Python book details, overriding the display_book method
    def display_python_book(self):
        # Calling the parent class method to get book info
        book_details = self.display_book()
        return f"{book_details}\nPrice: {self.price}\nNumber of Pages: {self.no_of_pages}"

# Main program
if __name__ == "__main__":
    # Creating an object of the Python class
    python_book = Python("P123", "TechBooks", "Learning Python", "John Doe", 599.99, 350)
    
    # Displaying information about the Python book
    print(python_book.display_publisher())
    print(python_book.display_python_book())

