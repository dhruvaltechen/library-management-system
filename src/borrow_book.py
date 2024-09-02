from _globals._books import AVAILABLE_BOOKS

def borrow_book(isbn):
    if len(AVAILABLE_BOOKS) == 0:
        print('No Books Available')
        return
    for book in AVAILABLE_BOOKS:
        if book['isbn'] == isbn:
            AVAILABLE_BOOKS.remove(book)
            print(book['title'], 'by', book['author'], 'borrowed successfully')
            return book
    return None