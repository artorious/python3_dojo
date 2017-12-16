#!/usr/bin/env python3
'''GCD-Compute greatest common factor of two integers provided by the user'''

from custom_modules.get_integer_from_user import get_integer
print(__doc__)

def gcd(num1, num2):
    '''Computes greatest common factor of two integers'''
    min_num = num1 if num1 < num1 else num2 # Determine the smalller value
    largest_factor = 1 # Universal factor
    for potential_gcd in range(1, min_num + 1): # Consider every int less than the smaller of the two values
        if num1 % potential_gcd == 0 and num2 % potential_gcd == 0:
            largest_factor = potential_gcd # Re-assign 
    return largest_factor 

if __name__ == '__main__':
    print('First Integer')
    n1 = get_integer()
    print('Second Integer')
    n2 = get_integer()
    print()
    print('gcd({0} and {1}) = {2}'.format(n1, n2, gcd(n1, n2)))
    