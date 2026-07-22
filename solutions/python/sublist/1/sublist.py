"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    ''' Returns if list one is equal, a sublist, a super list or not equal to list two'''
    if list_one == list_two:
        return EQUAL
    if list_one == []:
        return SUBLIST
    if list_two == []:
        return SUPERLIST
    if is_sublist(list_one, list_two):
        return SUBLIST
    if is_sublist(list_two, list_one):
        return SUPERLIST
  
    return UNEQUAL

def is_sublist(list_one, list_two):
    '''Returns true if list one is a sublist of list wo'''
    size_two = len(list_two)
    size_one = len(list_one)    
    return any(list_one == list_two[idx:idx+size_one] for idx in range(size_two-size_one+1))
