from _globals._books import AVAILABLE_BOOKS, ALL_BOOKS_ISBN

def add_book(isbn, title, author, publication_year):
    if isbn in [book['isbn'] for book in ALL_BOOKS_ISBN]:
        print('Book already exists')
        return
    AVAILABLE_BOOKS.append({'isbn': isbn, 'title': title, 'author': author, 'publication_year': publication_year})