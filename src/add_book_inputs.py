from utils.book_name_validator import book_name_validator
from utils.isbn_validator import isbn_validator
from utils.name_validator import name_validator
from utils.year_validator import year_validator

def add_book_inputs():
    isbn = input('Enter ISBN: ')
    while not isbn_validator(isbn):
        print('Invalid ISBN')
        isbn = input('Enter ISBN: ')
    title = input('Enter title: ')
    while not book_name_validator(title):
        print('Invalid title')
        title = input('Enter title: ')
    author = input('Enter author: ')
    while not name_validator(author):
        print('Invalid author')
        author = input('Enter author: ')
    publication_year = input('Enter publication year: ')
    while not year_validator(publication_year):
        print('Invalid year')
        publication_year = input('Enter publication year: ')
    return isbn, title, author, int(publication_year)