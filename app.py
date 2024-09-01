from src.add_book_inputs import add_book_inputs
from src.add_books import add_book
from src.borrow_book import borrow_book
from src.return_book import return_book
from src.view_available_books import view_available_books

while True:
    try:
        operation = int(input("1. Add book\n2. Borrow book\n3. Return book\n4. View available books\n5. Exit\nEnter your choice: "))
        match operation:
            case 1:
                isbn, title, author, publication_year = add_book_inputs()
                add_book(isbn, title, author, publication_year)
            case 2:
                isbn = input('Enter ISBN: ')
                borrow_book(isbn)
            case 3:
                isbn = input('Enter ISBN: ')
                return_book(isbn)
            case 4:
                view_available_books()
            case 5:
                print("Thanks for using the library management system")
                break
            case _:
                print("Invalid choice")
    except Exception as e:
        print(e)