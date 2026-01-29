class LibraryBook:
    """Library system class: OOP with encapsulation, methods, exception handling."""

    def __init__(self, book_id: str, title: str, author: str, is_available: bool = True):
        """Initialize book (ENCAPSULATION: private attributes)."""
        if not all([book_id, title, author]):
            raise ValueError("Book ID, title, and author required.")
        self._book_id = book_id
        self._title = title
        self._author = author
        self._is_available = is_available
        self._borrow_history = []  # Encapsulated transaction log

    def borrow(self, borrower: str) -> bool:
        """Borrow method (OOP operation, TRY-EXCEPT)."""
        try:
            if not borrower:
                raise ValueError("Borrower name required.")
            if not self._is_available:
                raise ValueError(f"Book '{self._title}' not available.")
            self._is_available = False
            self._borrow_history.append(f"Borrowed by {borrower}")
            print(f"[SUCCESS] Borrowed '{self._title}' to {borrower}")
            return True
        except ValueError as e:
            print(f"[ERROR] {e}")
            return False

    def return_book(self) -> bool:
        """Return method (OOP operation, exception handling)."""
        try:
            if self._is_available:
                raise ValueError(f"Book '{self._title}' already available.")
            self._is_available = True
            self._borrow_history.append("Returned")
            print(f"[SUCCESS] Returned '{self._title}'")
            return True
        except ValueError as e:
            print(f"[ERROR] {e}")
            return False

    def get_status(self) -> str:
        """Getter for status (ENCAPSULATION)."""
        return "Available" if self._is_available else "Borrowed"

    def display_info(self):
        """Display book details."""
        status = self.get_status()
        print(f"\nBook ID: {self._book_id}")
        print(f"Title: {self._title} by {self._author}")
        print(f"Status: {status}")
        print()

    def show_history(self):
        """Show borrow history."""
        print(f"\nHistory for '{self._title}':")
        if not self._borrow_history:
            print("No borrows yet.")
        else:
            for i, event in enumerate(self._borrow_history, 1):
                print(f"{i}. {event}")
        print()

def get_string_input(prompt: str) -> str:
    """Safe string input with validation."""
    while True:
        try:
            val = input(prompt).strip()
            if not val:
                print("Input cannot be empty.")
                continue
            return val
        except KeyboardInterrupt:
            print("\nCancelled.")
            raise

def get_choice_input(prompt: str, options: list) -> str:
    """Safe choice input (TRY-EXCEPT)."""
    while True:
        try:
            choice = input(prompt).strip()
            if choice not in options:
                print(f"Choose from: {', '.join(options)}")
                continue
            return choice
        except ValueError:
            print("Invalid input.")

def main():
    """Main menu: OOP class usage, user input, error handling."""
    print("LIBRARY MANAGEMENT SYSTEM")
    
    book_id = get_string_input("Book ID: ")
    title = get_string_input("Title: ")
    author = get_string_input("Author: ")
    
    try:
        book = LibraryBook(book_id, title, author)  # OOP: Instantiate object
        print("[SUCCESS] Book added!")
    except ValueError as e:
        print(f"[ERROR] {e}")
        return
    
    while True:
        print("\n1. Borrow  2. Return  3. Status  4. Info  5. History  6. Exit")
        choice = get_choice_input("Choice: ", ['1', '2', '3', '4', '5', '6'])
        
        if choice == '1':
            borrower = get_string_input("Borrower name: ")
            book.borrow(borrower)
        elif choice == '2':
            book.return_book()
        elif choice == '3':
            print(f"Status: {book.get_status()}")
        elif choice == '4':
            book.display_info()
        elif choice == '5':
            book.show_history()
        elif choice == '6':
            print("Thank you!")
            break

if __name__ == "__main__":
    main()
