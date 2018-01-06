#!/usr/bin/env python3
""" Test Floating-point Equality """
from math import fabs

def float_equality(float1, float2, tolerance):
    """
    Returns True if <float1> = <float2> or |<float1> - <float2>| < <tolerance>
    
    If <float1> and <float2> differ by only a small amount(specified by 
    <tolerance>), <float1> and <float2> are considered "equal". 
    NOTE:
        Useful to account for floating-point round-off error.
        The == operator is checked first since some spaecial floating-point 
        values such as floating-point infinity require an exact equality check
    """

    return float1 == float2 or fabs(float1 - float2) < tolerance


if __name__ == '__main__':
    print(__doc__)
    # Init
    test_float = 0.0
    while not float_equality( test_float, 1.0, 0.0001):
        print("test_float =", test_float)
        test_float += 0.1