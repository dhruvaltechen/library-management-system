from _globals._books import AVAILABLE_BOOKS, ALL_BOOKS_ISBN

def borrow_book(isbn):
    for book in AVAILABLE_BOOKS:
        if book['isbn'] == isbn:
            AVAILABLE_BOOKS.remove(book)
            return book
    return None