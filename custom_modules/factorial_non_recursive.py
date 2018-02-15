#!/usr/bin/env python3
""" Factorial Function (non-recursive version). 

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

def factorial_v2(num):
    """ (int) -> float
    
        Computes num!
        Returns the factorial of <num>
    """
    if isinstance(num, int) and num >= 0:
        product = 1 # Init
        if num == 0:
            return product
        for a_num in range(num, 0, -1):
            product *= a_num
        return product
    else:
        return 'Expected Positive integer'

if __name__ == '__main__':
    from timer import Timer
    from get_integer_from_user import get_integer
    
    player = get_integer()
    t = Timer()
    print('Test-time factorial_n()')
    t.start()
    print(factorial_n(player))
    t.stop()
    print(t.elapsed())
    print('----------------------------')
    print('Test-time factorial_v2()')
    t.reset()
    t.start()
    print(factorial_v2(player))
    t.stop()
    print(t.elapsed())
    