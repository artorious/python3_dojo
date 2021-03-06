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
current_potential_prime = 2 # Smallest prime
max_value = int(get_positive_num())     # Get positive integer from user
cntr = 0 # Prime accumulator
start_stopwatch = clock()   # Start timer

##------- The Algorithm -------- ##

while current_potential_prime <= max_value:
    is_prime = True     # Provisionally, Assume value is prime
    
    # Try all possible factors from 2 to current_potential_prime - 1
    trial_factor = 2 # Track potential factors
    
    while trial_factor < current_potential_prime:
        if current_potential_prime % trial_factor == 0:
            is_prime = False    # Not a factor
            break   # No need to continue
        trial_factor += 1   # Try next potential factor
    
    if is_prime:
        print(current_potential_prime, end=' ')     # Dispaly the prime number
        cntr += 1 # Track total primes found
    current_potential_prime += 1    # Try the next potential prime

print() # Move cursor to the next line
stop_stopwatch = clock() - start_stopwatch # Stop timer
print('It takes {0} secs to identify {1} prime numbers'.format(stop_stopwatch, cntr))           
