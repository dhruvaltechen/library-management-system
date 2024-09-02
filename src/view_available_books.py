from _globals._books import AVAILABLE_BOOKS

def view_available_books():
    if len(AVAILABLE_BOOKS) == 0:
        print('No Books Available')
        return
    print('AVAILABLE BOOKS')
    for book in AVAILABLE_BOOKS:
        print(f'ISBN: {book["isbn"]}, Title: {book["title"]}, Author: {book["author"]}, Publication Year: {book["publication_year"]}')