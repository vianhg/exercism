''' Primes (Eratostenes'''

def primes(limit):
    '''Returns the list of primes up to limit'''
    numbers = set(range(2, limit+1))
    for idx in range(2, limit+1):
        if idx in numbers:
            for multiple in range(idx*2, limit+1, idx):
                numbers.discard(multiple)
    return list(numbers)


#import numpy as np

#def primes(limit):
#    numbers = np.array([True] * limit, dtype=bool)
#    for idx in range(2, limit+1):
#        if numbers[idx]:
#            for multiple in range(idx*2, limit, idx):
#                numbers[multiple] = False
#    return [ prime for prime in numbers if prime ]
