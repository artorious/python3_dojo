#!/usr/bin/env python3
""" Compute greatest common factor of two integers provided by the user """

from get_integer_from_user import get_integer

def gcd_recursive(num1, num2):
    """ (int, int) -> int

        Uses Euclid's method to compute the greatest common factor
        (greatest common divisor) of two integers, <num1> and <num2>
        Returns greatest common factor (gcd) of the two integers
    """
    if isinstance(num1, int) and isinstance(num2, int):
        if num1 == 0:
            return num2
        elif num2 == 0:
            return num1
        else:   
            if num1 > num2: # Handle RuntimeError: maximum recursion depth exceeded in comparison
                return gcd_recursive(num2, num1 % num2)
            else:
                return gcd_recursive(num1, num2 % num1)
    else:
        return 'Expected Two Integers'

def gcd_iterative(num1, num2):
    """ (int, int) -> int
    
        Uses a naive iterative algorithm to compute gcd of two integers, 
        <num1> and <num2>. 
        Returns greatest common factor (gcd) of the two integers
    """
    # TODO: Handle bug: gcd_iterative(900 and 0) = 0
    if isinstance(num1, int) and isinstance(num2, int):
        min_num = num1 if num1 < num1 else num2 # Determine the smalller value
        largest_factor = 1 # Universal factor
        for potential_gcd in range(1, min_num + 1): # Consider every int less than the smaller of the two values
            if num1 % potential_gcd == 0 and num2 % potential_gcd == 0:
                largest_factor = potential_gcd # Re-assign

        return largest_factor
    else:
        return 'Expected Two Integers'
        

     

if __name__ == '__main__':
    print(__doc__)
    # Init
    print('First Integer ->', end= ' ')
    arg1 = get_integer()
    print()
    print('Second Integer ->', end=' ')
    arg2 = get_integer()
    print()
    print('gcd_recursive({0} and {1}) = {2}'.format(arg1, arg2, gcd_recursive(arg1, arg2)))
    print(type(gcd_recursive(arg1, arg2)))
    print('gcd_iterative({0} and {1}) = {2}'.format(arg1, arg2, gcd_iterative(arg1, arg2)))
    print(type(gcd_iterative(arg1, arg2)))