#!/usr/bin/env python3
""" Fraction Objects
NOTE:
    The fractions module provides the Fraction class. 
    Fraction objects model mathematical rational numbers; that is, 
    the ratio of two integers. 
    Rational numbers contain a numerator and denominator.
"""
from fractions import Fraction

f1 = Fraction(3, 4)     # 3/4
print('Fraction(3, 4) :', f1)
print(f1.numerator)
print(f1.denominator)
print(float(f1))

f2 = Fraction(1, 8)
print("Fraction(1, 8) :", f2)
print()
print('{0} + {1} = {2}'.format(f1, f2, f1 + f2))

print()
print('Fraction(10, -8) :', Fraction(10, -8))
print('Fraction(Fraction(1, 7), 5) :', Fraction(Fraction(1, 7), 5))
print('Fraction(Fraction(1, 7), Fraction(2, 3)) :', Fraction(Fraction(1, 7), Fraction(2, 3)))
print('Fraction("314") :', Fraction('314'))
print('Fraction("-35/4") :', Fraction('-35/4'))
print('Fraction("3.1415") :', Fraction('3.1415')) # conversion from numeric string
print("Fraction('-47e-2') :", Fraction('-47e-2')) # string may include a decimal exponent
print('Fraction(1.47) : ', Fraction(1.47))  # direct construction from float (exactconversion)
print('Fraction(2.25) :', Fraction(2.25))
