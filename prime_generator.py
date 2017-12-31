#!/usr/bin/env python3
"""Experiments with the prime number generator"""

from custom_modules.primality_check import is_prime, prime_sequence
from custom_modules.get_positive_number_from_user import get_positive_num

print(__doc__)
print()
print('Enter a range of numbers min - max')
print()
print('Start Range: ', end='')
min_val = int(get_positive_num())
print('End Range: ', end='')
max_val = int(get_positive_num())
print()
sum_cntr = 0
threes = []
print('All the primes from {0} to {1}'.format(min_val, max_val))
for value in prime_sequence(min_val, max_val):
    print(value, end=' ')
    sum_cntr += value
    if value % 10 == 3:
        threes.append(value)
print()
print('Sum of primes from {0} to {1} = {2}'.format(min_val, max_val, sum_cntr))

print('All the primes from {0} to {1} that end in 3: {2}'.format(min_val, max_val, threes))