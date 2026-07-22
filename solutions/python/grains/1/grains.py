def square(number):
    if number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)


def total():    
    count = 1
    total = count
    for i in range(63):
        count *= 2
        total += count
    return total
