#!/usr/bin/env python3
""" A play at Rational numbers (Fractions)

Uses the Python’s dunder notation to better protect instance variables.
 
NOTE: 
    This form of protection (information hiding) defends against a 
    conscientious but careless programmer but not a malicious one.
"""

class Rational(object):
    """Represents a rational number (fraction)

    NOTE:
        A rational number is the ratio of two integers. 
        There is a restriction, however — the number on the bottom of a 
        fraction cannot be zero. The number on the top of the fraction is 
        called the numerator, and the bottom number is known as the 
        denominator. 
    """
    def __init__(self, numerator, denominator):
        """ (Rational, int, int) -> int, int 
        
        Inits Rational with values <numerator> and <denominator>
        """
        self.__numerator = numerator
        if denominator != 0:
            self.__denominator = denominator
        else:
            raise ValueError('DivisionByZeroError: zero cant be denominator')

    def get_numerator(self):
        """ (Rational) -> int

        Returns the numerator of the fraction.
        """
        return self.__numerator
    
    def get_denominator(self):
        """ (Rational) -> int

        Returns the denominator of the fraction.
        """
        return self.__denominator

    def set_numerator(self, value):
        """ (Rational, int) -> Rational

        Sets the numerator of the fraction to <value>.
        """
        self.__numerator = value

    def set_denominator(self, value):
        """ (Rational, int) -> Rational
        
        Sets the denominator of the fraction to <value>.
        Unless <value> is zero, then method terminates program with 
        error meassage
        """
        if value != 0:
            self.__denominator = value
        else:
            raise ValueError("DivisionByZeroError: zero cant be denominator")

    def reduce(self):
        """ Simplify Fraction """
        gcd = self.__calc_gcd()
        self.__numerator = self.__numerator // gcd
        self.__denominator = self.__denominator // gcd

    def __calc_gcd(self):
        """ Calculates GCD """
        a = max(self.__numerator, self.__denominator)
        b = min(self.__numerator, self.__denominator)

        while b != 0:
            temp = b
            b = a % b
            a = temp

        return a 

    def __repr__(self):
        """ (Rational) -> str

        Make a string representation of a Rational number x/y
        """
        return '{0}/{1}'.format(self.__numerator, self.__denominator)

    def __neg__(self):
        """ (Ratianal) -> Rational

        Returns a new fraction equal to the negation of self. 
        """
        return Rational(-self.__numerator, self.__denominator)

    def __add__(self, r_fraction):
        """ 
        Returns a new reduced fraction equal to <self> + <r_fraction>
        """
        numer = self.__numerator * r_fraction.get_denominator() +\
                r_fraction.get_numerator() * self.__denominator

        denom = self.__denominator * r_fraction.get_denominator()

        result_addition = Rational(numer, denom)
        result_addition.reduce()

        return result_addition
    
    def __sub__(self, r_fraction):
        """
        Returns a new reduced fracion equal to <self> - <r_fraction>
        """

        return self + (-r_fraction)

    def __multiply__(self, r_fraction):
        """ (Rational, Rational) -> Rational
        
        Returns a new rduced fraction equal to <self> * <r_fraction>
        """
        numer = self.__numerator * r_fraction.get_numerator()
        denom = self.__denominator * r_fraction.get_denominator()

        result_multiply = Rational(numer, denom)

        result_multiply.reduce()

        return result_multiply

# TODO: Add Relational operators to the fraction class    
def main():
    """ Client code that uses Rational objects """
    fract1 = Rational(1, 2)
    fract2 = Rational(1, 4)
    print('Fraction 1: {0}'.format(fract1))
    print('Fraction 2: {0}'.format(fract2))
    print('{0} * {1} = {2}'.format(fract1, fract2, Rational.__multiply__(fract1, fract2)))
    print('{0} + {1} = {2}'.format(fract1, fract2, Rational.__add__(fract1, fract2)))
    print('{0} - {1} = {2}'.format(fract1, fract2, Rational.__sub__(fract1, fract2)))
    print('Negate({0}) = {1}'.format(fract1, Rational.__neg__(fract1)))
        
    fract1.set_numerator(3)
    fract1.set_denominator(4)
    fract2.set_numerator(2)
    fract2.set_denominator(3)
    print('Fraction 1: {0}'.format(fract1))
    print('Fraction 2: {0}'.format(fract2))
    print('{0} * {1} = {2}'.format(fract1, fract2, Rational.__multiply__(fract1, fract2)))
    print('{0} + {1} = {2}'.format(fract1, fract2, Rational.__add__(fract1, fract2)))
    print('{0} - {1} = {2}'.format(fract1, fract2, Rational.__sub__(fract1, fract2)))
    print('Negate({0}) = {1}'.format(fract1, Rational.__neg__(fract1)))

    # fract_bad = Rational(4, 0)

if __name__ == '__main__':
    main()