from _globals._books import AVAILABLE_BOOKS, ALL_BOOKS_ISBN

def return_book(isbn):
    for book in AVAILABLE_BOOKS:
        if book['isbn'] == isbn:
            print('Book is already retured')
            return book
    for book in ALL_BOOKS_ISBN:
        if book['isbn'] == isbn:
            AVAILABLE_BOOKS.append(book)
            return book
    print('Book not found')