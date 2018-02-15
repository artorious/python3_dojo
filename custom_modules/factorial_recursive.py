#!/usr/bin/env python3
""" Factorial Function (recursive version). 
    
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
    # Check for valid input
    if isinstance(num, int) and num >= 0:
        # Base Case - terminates recursion
        if num == 0: 
            return 1
        # Breakdown
        else:
            return num * factorial_n(num - 1) # n*(n - 1)!
    
    else:
        return 'Expected Positive integer'

if __name__ == '__main__':
    # run
    from timer import Timer
    from get_integer_from_user import get_integer

    t = Timer()

    t.start()
    print(factorial_n(get_integer()))
    t.stop()
    print(t.elapsed())
    