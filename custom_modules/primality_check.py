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

def primes_list_comprehension(num):
    """ (int) - list

    For all num ≥ 2, the following list comprehension creates a list of 
    all the factors of n, not including 1 and n itself. 

    Builds and returns  a list that contains all the prime numbers less
    than <num>. 
    """
    return [p for p in range(2, num) if not [x for x in range(2, p) if p % x == 0]] 
    

# TODO:
def prime_seq_sieve(max_potential_prime):
    """ (int) -> list

    Prime Generation with a List - implements the Sieve of Eratosthenes 
    in a Python function.

    Uses an algorithm developed by the Greek mathematician Eratosthenes who 
    lived from 274 B.C. to 195 B.C. Called the Sieve of Eratosthenes, 
    the principle behind the algorithm is simple: 

    Make a list of all the integers two and larger. 
    Two is a prime number, but any multiple of two cannot be a prime number 
    (since a multiple of two has two as a factor). Go through the rest of the 
    list and mark out all multiples of two (4, 6, 8, ...). 
    Move to the next number in the list (in this case, three). 
    If it is not marked out, it must be prime, 
    so go through the rest of the list and mark out all multiples of that 
    number (6, 9, 12, ...). Continue this process until you have listed 
    all the primes you want.
    """
    pass
    

if __name__ == '__main__':
    from get_positive_number_from_user import get_positive_num
    num = int(get_positive_num())
    print(primes_list_comprehension(num))