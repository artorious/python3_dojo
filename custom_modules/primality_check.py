#!/usr/bin/env python3
"""Test for Primality.
Tests for primality each integer from 2 up to a value provided by the user.  
If an integer is prime, it prints it; otherwise, the number is not printed.
Note: 
    A prime number is an integer greater than 1 whose only factors (divisors)
    are 1 and the number itself
"""

from math import sqrt
from get_positive_number_from_user import get_positive_num

##################################################################################################

def is_prime(the_integer):
    """(int) -> bool
    Determines the primality of a given value <the_integer>, an integer.
    Returns True if <the_integer>, otherwise, returns False
    """
    if isinstance(the_integer, int):
        # Try potential factors from 2 (smallest prime) to the square root of <the_integer> (inclusive)
        # Use of squareroot to increase program efficiency (Instead of Trying values from 2  to <the_integer> (inclusive))
        root = round(sqrt(the_integer)) + 1 

        for trial_factor in range(2, root):
            if the_integer % trial_factor == 0:     # Is it a factor
                return False                        # Found a Factor
        return True                                 # No factors found
    else:
        return 'Expected an integer. {0} not surpported'.format(type(the_integer))
    

######################################################################################################

def main():
    """Check for Primality"""
    print(__doc__) # Program Greeting

    # Init
    max_value = int(get_positive_num())

    for value in range(2, max_value + 1):   # Step thro all potential primes
        if is_prime(value):                 # Check if prime
            print(value, end=" ")           # Display primes found
    print()                                 # Move cursor to the  next line

if __name__ == '__main__':
    main()