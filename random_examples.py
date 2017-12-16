#!/usr/bin/env python3
'''Random Numbers
random - python module. A Pseudorandom number generator
'''

from random import randrange, seed, choice
import sys



# Init
terminate = False

while not terminate:
    print(__doc__) # Program Greeting

    print(format(' Print 100 random number Range 1..1000 (inclusive) ', '~^120'))
    seed(23) # Set random number seed. Determine the exact sequence of numbers the program generates
    for random_num in range(0, 100): # No. of iterations
        print(randrange(1, 1001), end=' ')  # Display No.s
    print('\n')
    seed() # Seed from current time
    print(format(' Select a random element from a tuple of strings ', '~^120'))
    for random_str in range(10): # No. of iterations
        print(choice(('one', 'two', 'three', 'four', 'five', 'six', 
                'seven', 'eight', 'nine', 'ten')), end=' ') # Choose random str from object
    print('\n')

    exit_program = input('Press Enter to Run Again, Q/q to Quit: ')
    
    if exit_program in ['q', 'Q']:
        sys.exit(0)
    elif exit_program == '':
        continue
    else:
        continue

