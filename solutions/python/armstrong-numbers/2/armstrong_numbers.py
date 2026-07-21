def is_armstrong_number(n):
    '''Returns true if n is a armstrong number'''
    sum_of_pow_digits = 0
    digits = str(n)
    lenght = len(digits)
    for digit in digits:
        sum_of_pow_digits += int(digit)**lenght
    return n == sum_of_pow_digits
