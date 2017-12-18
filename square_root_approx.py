#!/usr/bin/env python3
""" Square root Examples.

Note: The strategy;
    1. Guess the square root.
    2. Square the guess and see how close it is to the original number;
        If it is close enough to the correct answer, STOP.
    3. Make new guess that will produce a better result & proceed with step 2
"""
from custom_modules.get_positive_number_from_user import get_positive_num

def square_root(value):
    """ (float) -> float
    Compute an approximation of the square root of <value> 
    """
    # Init
    root = 1.0  # Provisional square root
    difference = (root * root) - value  # How far off is our provisional root

    ##--- Loop until the provisional root is close enough to the actual root ----###
    while difference > 0.00000001 or difference < -0.00000001:
        root = (root + (value / root)) / 2  # Compute new provisional root
        difference = (root * root) - value # # How far off is our current approximation?
    
    return root

if __name__ == '__main__':
    from math import sqrt

    print(__doc__) # Program Greeting
    print(format(' Compare Approx roots and actual roots ', '|^60'))

    # Init
    start_point = 1.0 # Set point to begin
    print('Calculate the roots up to (Max Value) : ', end=' ')
    max_value = get_positive_num() # Get positive Float from user
    print()
    print(' Value  :  Approximate root :  Actual root ')
    print('_' * 60)
    while start_point <= max_value:
        print('{0:6.1f} : {1:16.8f} : {2:16.8f} '.format(start_point, square_root(start_point), sqrt(start_point)))
        start_point += 0.5  # next value



