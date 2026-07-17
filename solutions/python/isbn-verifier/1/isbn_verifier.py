import re
def is_valid(isbn):
    if not re.match(r"^\d-?\d{3}-?\d{5}-?[\dX]$", isbn):
        return False
    sum = 0
    isbndigits = isbn.replace('-', '')
    for i in range(0, 10):
        d = '10' if (isbndigits[i] == 'X' and i == 9) else isbndigits[i]        
        sum += (10-i) * int(d)
    return sum % 11 == 0
