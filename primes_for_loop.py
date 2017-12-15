#!/usr/bin/env python3
'''Prints all the primes numbers up to a value supplied from the user
Note: 
    A prime number is an integer greater than 1 whose only factors (divisors)
    are 1 and the number itself
'''

from custom_modules.get_positive_number_from_user import get_positive_num

print(__doc__) # Program Greeting
# init --Get positive integer from user
max_value = int(get_positive_num())


##------- The Algorithm -------- ##

# Try values from 2 (smallest prime) to max_value (inclusive)
for potential_prime in range(2, max_value + 1):
    is_prime = True     # Provisionally, assume it is prime
    for trial_factor in range(2, potential_prime):  # Try all possible factors from 2 to  potential_prime - 1
        if potential_prime % trial_factor == 0: 
            is_prime = False
            break      # no need to continue
    if is_prime:
        print(potential_prime, end=' ')  # Display prime
print() # Move cursor to the next line
        
    

