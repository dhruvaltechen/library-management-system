def isbn_validator(isbn):
    isbn = isbn.replace("-", "")
    conditions = [len(isbn) == 13, isbn[0:3] == "978" or isbn[0:3] == "979", isbn.isdigit()]
    print(conditions)
    return all(conditions)