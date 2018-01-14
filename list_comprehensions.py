#!/usr/bin/env python3
""" A Play on Python List Comprehensions """

from custom_modules.get_positive_number_from_user import get_positive_num

def factors_singles(num):
    """ (int) -> list
    
    Builds a list of factors for a positive integer <num>. 
    Returns the list
    """
    return [x for x in range(1, num + 1) if num % x == 0]

def main():
    """ A Play on Python List Comprehension """
    n = int(get_positive_num())
    print('Factors of {0}: {1}'.format(n, factors_singles(n)))

if __name__ == '__main__':
    main()