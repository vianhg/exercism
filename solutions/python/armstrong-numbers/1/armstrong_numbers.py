def is_armstrong_number(n):
    '''Returns true if n is a armstrong number'''
    sum = 0
    digits = str(n)
    lenght = len(digits)
    for d in digits:
        sum += int(d)**lenght
    return n == sum
