def book_name_validator(name):
    if name.isdigit() and len(name) == 0:
        return False
    return True