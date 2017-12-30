#!/usr/bin/env python3
"""Factorial Function (non-recursive version). 
NOTE:
The factorial of n is expressed as n!
Factorial is defined for a non-negative integer as;
    n! = n * (n - 1) * (n - 2) * (n - 3) ... 3 * 2 * 1
and 0! is defined as 1. Thus;
    6! = 6*5*4*3*2*1
    6! = 720
Therefore:
    n! is 1, if n = 0
    n! is n*(n - 1)!, otherwise.
"""

def factorial_n(num):
    """ (int) -> float
    Computes num!
    Returns the factorial of <num>
    """
    if isinstance(num, int) and num >= 0:
        product = 1 # Init
        while num: # As long as num is positive
            product *= num
            num -= 1
        return product
    else:
        return 'Expected Positive integer'

if __name__ == '__main__':
    print(__doc__)
    
    from get_integer_from_user import get_integer
    
    print(factorial_n(get_integer()))