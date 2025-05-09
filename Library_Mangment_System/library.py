class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self.borrow_limit = 2 

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.borrow_limit:
            print("Borrowing limit reached!")
            return
        if book.is_borrowed:
            print("Book is already borrowed!")
            return
        book.is_borrowed = True
        self.borrowed_books.append(book)
        print(f"Borrowed: {book.title}")

    def return_book(self, book):
        if book not in self.borrowed_books:
            print("You haven't borrowed this book!")
            return
        book.is_borrowed = False
        self.borrowed_books.remove(book)
        print(f"Returned: {book.title}")

    def check_borrowed_books(self):
        if not self.borrowed_books:
            print("No books borrowed.")
        else:
            print("Books borrowed:", ", ".join(book.title for book in self.borrowed_books))

class PremiumMember(LibraryMember):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self.borrow_limit = 5 
