from library import *

def main():
    books = [Book("1984"), Book("Moby Dick")]
    members = {
        "1": LibraryMember("Alice", "1"),
        "2": PremiumMember("Bob", "2")
    }

    while True:
        member_id = input("Enter Member ID (or 'exit' to quit): ")
        if member_id == "exit":
            break
        if member_id not in members:
            print("Invalid Member ID!")
            continue

        member = members[member_id]
        action = input("Enter 'b' to borrow, 'r' to return, 'c' to check books, or 'exit' to quit: ")

        if action == "b":
            book_title = input("Enter book title to borrow: ")
            book = next((b for b in books if b.title == book_title), None)
            if book:
                member.borrow_book(book)
            else:
                print("Book not found!")
        elif action == "r":
            book_title = input("Enter book title to return: ")
            book = next((b for b in member.borrowed_books if b.title == book_title), None)
            if book:
                member.return_book(book)
            else:
                print("Book not found in borrowed list!")
        elif action == "c":
            member.check_borrowed_books()
        elif action == "exit":
            break
        else:
            print("Invalid input!")

if __name__ == "__main__":
    main()
