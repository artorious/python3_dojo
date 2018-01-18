#!/usr/bin/env python3
""" A play at Rational numbers (Fractions)

Uses the Python’s dunder notation to better protect instance variables. 
NOTE: 
    This form of protection defends against a conscientious but careless
    programmer but not a malicious one.
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
        """ (Rational, int, int) -> Init 
        
        Initialization function
        """
        self.__numerator = numerator
        if denominator != 0:
            self.__denominator = denominator
        else:
            raise ValueError('Attempt to make an illegal rational number')
    
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

    def set_numerator(self, numerator):
        """ (Rational, int) -> Rational

        Sets the numerator of the fraction to <numerator>.
        """
        self.__numerator = numerator
    
    def set_denominator(self, denominator):
        """ (Rational, int) -> Rational
        
        Sets the denominator of the fraction to <denominator>.
        Unless <denominator> is zero, then meyhod terminates program with 
        error meassage
        """
        if denominator != 0:
            self.__denominator = denominator
        else:
            raise ValueError("Error: zero cant be denominator")

    def __multiply__(self, other_fraction):
        """ (Rational, Rational) -> Rational
        
        Returns the product of this rational number object the 
        <other_fraction> rational object.
        """
        return Rational(
                self.__numerator * other_fraction.__numerator, 
                self.__denominator * other_fraction.__denominator)

    def __add__(self, other_fraction):
        """ (Rational, Rattional) -> Rational

        Returns the sum of this rational number object with the
        <other_fraction> rational object.
        """
        pass

    def __str__(self):
        """ (Rational) -> str

        Make a string representation of a Rational number
        """
        return '{0}/{1}'.format(str(self.get_numerator()), str(self.get_denominator())) 

def main():
    """ Client code that uses Rational objects """
    fract1 = Rational(1, 2)
    fract2 = Rational(2, 3)
    print('Fraction 1: {0}'.format(fract1))
    print('Fraction 2: {0}'.format(fract2))

    fract1.set_numerator(3)
    fract1.set_denominator(4)
    fract2.set_numerator(1)
    fract2.set_denominator(10)
    print('Fraction 1: {0}'.format(fract1))
    print('Fraction 2: {0}'.format(fract2))

    fract3 = Rational(1, 2)
    fract4 = Rational(3, 5)
    print('{0} * {1} = {2}'.format(fract3, fract4, Rational.__multiply__(fract3, fract4)))

    fract5 = Rational(1, 2)
    fract6 = Rational(1, 2)
    print('{0} * {1} = {2}'.format(fract5, fract6, Rational.__multiply__(fract5, fract6)))

    # fract_bad = Rational(4, 0)

if __name__ == '__main__':
    main()