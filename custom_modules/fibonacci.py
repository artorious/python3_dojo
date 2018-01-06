#!/usr/bin/env python3
""" A recursive play at the infinite fibonacci sequence.

    Computes the nth fibonacci number.
    NOTE:
    Fibonacci numbers is a sequence of integers beginning with 0 followed by 1
    Subsequent elements of the sequence are the sum of their two immediately 
    preceding elements. Thus the 3rd number is 0+1=1, the 4th number is 1+1=2,
    the 5th number is 1+2=3, etc. 
    NOTE: Zero is the 0th, 1 is the 1st, 1 is also the 2nd, 2 is 3rd, 3 is 4th, 
    5 is 5th, etc.
        0,1,1,2,3,5,8,13,21,34,55,89,144,.......
"""

def fibonacci(nth_fib):
    """ (int) -> int
    
        where <nth_fib> is a positive integer,
        Returns the <nth_fib> Fibonacci number
    """
    if isinstance(nth_fib, int):
        if nth_fib < 0:
            return 0
        elif nth_fib == 1:
            return 1
        else:
            return fibonacci(nth_fib - 2) + fibonacci(nth_fib - 1)
    else:
        return 'Expected Integer'

if __name__ == '__main__':
    from get_integer_from_user import get_integer
    print(__doc__)
    print('Calculate the nth Fibonacci Number: ', end='')
    print(fibonacci(get_integer()))