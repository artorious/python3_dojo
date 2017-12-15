#!/usr/bin/env python3
'''Prints all the primes numbers up to a value supplied from the user
Note: 
    A prime number is an integer greater than 1 whose only factors (divisors)
    are 1 and the number itself
'''

from custom_modules.get_positive_number_from_user import get_positive_num
from time import clock

print(__doc__) # Program Greeting
# init 
max_value = int(get_positive_num()) # Get positive integer from user
cntr = 0 # Prime accumulator
start_stopwatch = clock()   # Start timer
##------- The Algorithm -------- ##

# Try values from 2 (smallest prime) to max_value (inclusive)
for potential_prime in range(2, max_value + 1):
    is_prime = True     # Provisionally, assume it is prime
    for trial_factor in range(2, potential_prime):  # Try all possible factors from 2 to  potential_prime - 1
        if potential_prime % trial_factor == 0: 
            is_prime = False
            break      # no need to continue
    if is_prime:
        cntr += 1 # Track total primes found
        print(potential_prime, end=' ')  # Display prime
print() # Move cursor to the next line
stop_stopwatch = clock() - start_stopwatch # Stop timer
print('It takes {0} secs to identify {1} prime numbers'.format(stop_stopwatch, cntr))
    

