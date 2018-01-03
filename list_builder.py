#!/usr/bin/env python3
""" A play on python lists
Build custom lists as specified by the user
"""


def build_list_of_positive_integers():
    """(None) -> list
    Builds a list of non-negative integers from input provided by user
    Returns the list
    """
    
    result = [] # Init empty list
    in_val = 0 # Ensure loop is entered atleast once

    while in_val >= 0:
        
        try:
            in_val = int(input('Enter positive integer (-1 quits): '))
            
            if in_val >= 0:         # Check for positive int, else exit loop
                result += [in_val]  # Add item to list

        except ValueError as verr:
            print('Expected positive Integer...{0}'.format(verr))
            print('Try again')
            continue # 
        
    return result

if __name__ == '__main__':
    from custom_modules.primality_check import is_prime, prime_sequence
    
    # Make a list from a generator
    primes = list(prime_sequence(20, 50))
    print(primes)
    