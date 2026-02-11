class Book:
    def __init__(self, book_title, author, publication_year):
        self.book_title = book_title
        self.author = author
        self.publication_year = publication_year
        self.available = True

    def display_info(self):
        status = "Available" if self.available else "Not Available"
        print(f"Book Title: {self.book_title} Author: {self.author} Publication Year: {self.publication_year}")
        
    def borrow_book(self):
        if self.available:
            self.available = False
        print(f"You borrowed the book: {self.book_title} by {self.author}")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You returned the book: {self.book_title}")
        else:
            print(f"The book {self.book_title} is now available")
    
    def is_available(self):
        if self.available:
            print(f"The book {self.book_title} is avaiable")
        else:
            print(f"The book {self.book_title} is not available")

book_title = input("Book Title : ")
author = input("Author : ")
publication_year = input("Publication Year : ")


library_bms = Book(book_title, author, publication_year)

while True:
    print("\nPick an option: ")
    print("[1] Borrow a Book")
    print("[2] Return a Book")
    print("[3] Display Book Information")
    print("[4] Exit")
    option = input("Pick an option: ")

    if option == "1":
        library_bms.borrow_book()
        library_bms.is_available()
    elif option == "2":
        library_bms.return_book()
        library_bms.is_available()
    elif option == "3":
        library_bms.display_info()
        library_bms.is_available()
    elif option == "4":
         print("Library Management System Closed")
         break
    else:
        print("Your Choice is not valid")