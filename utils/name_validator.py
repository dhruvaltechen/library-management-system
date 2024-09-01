def name_validator(name):
    conditions = [len(name) > 0, not name.isdigit()]
    return all(conditions)