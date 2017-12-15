#!/usr/bin/env python3
'''Computes the square root of a number supplied by the user.
Strategy:
    1. Guess the square root.
    2. Square the guess and see how close it is to the original number;
        If it is close enough to the correct answer, STOP.
    3. Make new guess that will produce a better result & proceed with step 2
'''
from custom_modules.get_positive_number_from_user import get_positive_num

print(__doc__) # Program Greeting
# Init 
root = 1.0  # Provisional square root


value = get_positive_num() # Get positive Float from user 

difference = (root * root) - value  # How far off is our provisional root

##--- Loop until the provisional root is close enough to the actual root ----###

while difference > 0.00000001 or difference < -0.00000001:
    print('{0:,.3f} squared is {1:,.3f}'.format(root, root * root)) # Report
    root = (root + (value / root)) / 2  # Compute new provisional root
    difference = (root * root) - value # # How far off is our current approximation?

print('Approx. Square root of {0:,.3f} = {1:,.3f}'.format(value, root))


