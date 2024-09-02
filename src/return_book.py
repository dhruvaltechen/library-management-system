from _globals._books import AVAILABLE_BOOKS, ALL_BOOKS_ISBN

def return_book(isbn):
    for book in AVAILABLE_BOOKS:
        if book['isbn'] == isbn:
            print(book['title'], 'by', book['author'], 'is alrady returned')
            return book
    for book in ALL_BOOKS_ISBN:
        if book['isbn'] == isbn:
            AVAILABLE_BOOKS.append(book)
            print(book['title'], 'by', book['author'], 'returned successfully')
            return book
    print('Book not found')