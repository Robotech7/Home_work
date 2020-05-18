import re
def validate(email):
    pattern = r"^([a-zA-Z0-9_-])+@([a-z0-9])+(\.[a-z0-9]{1,3}$)"
    regex = re.compile(pattern)
    return regex.match(email)


