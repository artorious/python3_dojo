#!/usr/bin/env python3
'''Random Numbers
random - python module. A Pseudorandom number generator
'''

from random import randrange, seed

seed(23) # Set rndom number seed. Determine the exact sequence of numbers the program generates
for i in range(0, 100): # Print 100 random numbers
    print(randrange(1, 1001), end=' ') # Range 1..1000 (inclusive)
print()

    