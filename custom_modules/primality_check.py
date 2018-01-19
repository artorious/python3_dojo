#!/usr/bin/env python3
"""Tests for Primality.

    Note: 
        A prime number is an integer greater than 1 whose only factors 
        (divisors) are 1 and the number itself
"""

from math import sqrt
from stopwatch import Stopwatch

def is_prime(num):
    """ (int) -> bool
    
        Determines the primality of a positive value <num>, an integer
        Returns True if <num> is a prime number. Otherwise, 
        returns False
    """
    if isinstance(num, int) and num > 1:
        # Try potential factors from 2 (smallest prime) to the square root of 
        # <num> (inclusive) 
        # Use of squareroot to increase program efficiency (Instead of Trying 
        # values from 2  to <num> (inclusive))
        root = round(sqrt(num)) + 1 

        for trial_factor in range(2, root):
            if num % trial_factor == 0:     # Is it a factor
                return False       # Found a Factor
        return True           # No factors found
    else:
        return 'Expected a positive integer. {0} not surpported'.format(num)
    
def prime_generator(start, stop):        
    """ (int, int) -> generator

        Generates the sequence of prime numbers between <start> and <stop> (inclusive)
        Returns the generator object
    """
    for value in range(start, stop + 1):
        if is_prime(value) == True:
            yield value

def primes_list_comprehension(num):
    """ (int) - list

    For all num ≥ 2, the following list comprehension creates a list of 
    all the factors of n . 

    Builds and returns  a list that contains all the prime numbers less
    than <num> (inclusive). 
    """
    return [prime for prime in range(2, num + 1)  if not [potential for \
        potential in range(2, prime) if prime % potential == 0]] 

# TODO:
def prime_seq_sieve(num):
    """ (int) -> tuple

    Generates all the prime numbers from 2 to <num> (inclusive).
    <num> is the largest potential prime considered.
    Algorithm originally developed by Eratosthenes.

    Returns (prime_counter, primes_list) where prime_counter is the number of
    primes and primes_list is a list of the primes found

    NOTE:
        Uses an algorithm developed by the Greek mathematician Eratosthenes 
        who lived from 274 B.C. to 195 B.C. Called the Sieve of Eratosthenes, 
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

def main():
    """ Count the number of prime numbers less than two million and time
    how long it takes. Compares the performance of different algorithms
    """
    from get_positive_number_from_user import get_positive_num

    player_int = int(get_positive_num())
    timer = Stopwatch()
    print()
    print(format(' TimeIt - is_prime() ', '*^70'))
    timer.start() 
    print('{0} Is prime?: {1}'.format(player_int, is_prime(player_int)))
    timer.stop()
    print('Time taken = {0:.6f} Seconds'.format(timer.elapsed()))
    
    print()
    print(format(' TimeIt - prime_generator() ', '*^70'))
    timer.start()
    prime_gen_obj = prime_generator(0, player_int)
    timer.stop()
    print('{0} primes between 0 -> {1}'.format(
        len([t for t in prime_gen_obj]), player_int))
    print('Time taken = {0:.6f} Seconds'.format(timer.elapsed()))
    
    print()
    print(format(' TimeIt - primes_list_comprehension() ', '*^70'))
    timer.start()
    primes_list = primes_list_comprehension(player_int)
    timer.stop()
    print('{0} primes under {1}'.format(len(primes_list), player_int))
    print('Time taken = {0:.6f} Seconds'.format(timer.elapsed()))
    
    print()
    # 
    # 
    
    # 
    # 


if __name__ == '__main__':
    main()