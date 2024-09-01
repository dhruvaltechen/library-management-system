def year_validator(year):
    if year.isdigit() and len(year) == 4:
        return True
    return False