#!/usr/bin/env python3
'''Prints all the integers and their associated factors from 1-n'''
from custom_modules.get_positive_number_from_user import get_positive_num

print(__doc__) # Program Greeting
# init
count = 1 # Start from 1 (The numbers being examined)
value = int(get_positive_num()) # Get positive integer from user 

##------- The Algorithm -------- ##

while count <= value:                              # Dont go past max
    factor = 1                                     # 1 is a universal factor
    print('{0:>3}: '.format(repr(count)), end='')  # Which integer are we examining?
    while factor <= count:                         # Factors are <= the number being examined
        if count % factor == 0:                    # Test whether factor is a factor of the number being examined
            print(factor, end=' ')                 # Dispaly the factor if yes
        factor += 1                                # Try next possible factor
    print()                                        # Move to the next line
    count += 1                                     # Examine next number

    