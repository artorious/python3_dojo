#!/usr/bin/env python3
""" A Play on Python List Comprehensions """

from custom_modules.get_positive_number_from_user import get_positive_num
import math

def factors_singles(num):
    """ (int) -> list
    
    Builds a list of factors for a positive integer <num>. 
    Returns the list
    """
    return [x for x in range(1, num + 1) if num % x == 0]

def factors_pairs(num):
    """ (int) -> list
    Builds a list of factor pairs for a positive integer <num>. 
    for example, tuple (2, 15) is a factor pair for the number 30 
    because 2 x 15 is 30.

    Returns the list of factor-pair tuples
    """
    return [(x, num//x) for x in range(1, num + 1) if num % x == 0]

def unique_factor_pairs(num):
    """ (int) -> list
    Builds a list of unique factor pairs for a positive integer <num>. 
    for example, tuple (2, 15) is a factor pair for the number 30 
    because 2 x 15 is 30.

    Returns the list of unique factor-pair tuples
    """
    return [(x, num//x) for x in range(1, round(math.sqrt(num)) + 1) if num % x == 0]

def main():
    """ A Play on Python List Comprehension """
    n = int(get_positive_num())
    print('Factors of {0}: {1}'.format(n, factors_singles(n)))
    print('Factor pairs of {0}: {1}'.format(n, factors_pairs(n)))
    print('Unique Factor pairs of {0}: {1}'.format(n, unique_factor_pairs(n)))

if __name__ == '__main__':
    main()