#!/usr/bin/env python3
"""Tests for Primality.

    Note: 
        A prime number is an integer greater than 1 whose only factors 
        (divisors) are 1 and the number itself
"""

from math import sqrt

def is_prime(the_integer):
    """ (int) -> bool
    
        Determines the primality of a positive value <the_integer>, an integer
        Returns True if <the_integer> is a prime number. Otherwise, 
        returns False
    """
    if isinstance(the_integer, int) and the_integer > 1:
        # Try potential factors from 2 (smallest prime) to the square root of <the_integer> (inclusive)
        # Use of squareroot to increase program efficiency (Instead of Trying values from 2  to <the_integer> (inclusive))
        root = round(sqrt(the_integer)) + 1 

        for trial_factor in range(2, root):
            if the_integer % trial_factor == 0:     # Is it a factor
                return False                        # Found a Factor
        return True                                 # No factors found
    else:
        return 'Expected a positive integer. {0} not surpported'.format(the_integer)
    

def prime_sequence(start, stop):        
    """ (int, int) -> generator

        Generates the sequence of prime numbers between <start> and <stop>
        Returns the generator object
    """
    for value in range(start, stop):
        if is_prime(value) == True:
            yield value


    
    

if __name__ == '__main__':
    from get_positive_number_from_user import get_positive_num

    print("Check for Primality") # Program Greeting

    # Init
    max_value = int(get_positive_num())

    cntr = 0

    for value in range(2, max_value + 1):   # Step thro all potential primes
        if is_prime(value):                 # Check if prime
            cntr += value
            print(value, end=" ")           # Display primes found
    print()                                 # Move cursor to the  next line
    print('Total =', cntr)