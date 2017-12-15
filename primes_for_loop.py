#!/usr/bin/env python3
'''Prints all the primes numbers up to a value supplied from the user
Note: 
    A prime number is an integer greater than 1 whose only factors (divisors)
    are 1 and the number itself
'''

print(__doc__) # Program Greeting
# init
valid_value = False

##------ Get positive integer from user ------- ###
while not valid_value:
    try:
        max_value = int(input('Enter an integer Value: '))  # Enter Max value
        if max_value > 0:
            valid_value = True # Terminate loop after getting a valid value
        else:
            print('Please enter a positive integer')
            continue # Try entering value again

    except ValueError:
        print('Expected integers...')

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
        
    

