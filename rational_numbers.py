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
        pass
    
    def get_numerator(self):
        """ (Rational) -> int

        Returns the numerator of the fraction.
        """
        return

    def get_denominator(self):
        """ (Rational) -> int

        Returns the denominator of the fraction.
        """
        return

    def set_numerator(self, numerator):
        """ (Rational, int) -> Rational

        Sets the numerator of the fraction to <numerator>.
        """
        pass
    
    def set_denominator(self, denominator):
        """ (Rational, int) -> Rational
        
        Sets the denominator of the fraction to <denominator>.
        Unless <denominator> is zero, then meyhod terminates program with 
        error meassage
        """
        pass

    def __multiply__(self, other_fraction):
        """ (Rational, Rational) -> Rational
        
        Returns the product of this rational number object the 
        <other_fraction> rational object.
        """
        return

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
        pass

def main():
    """ Client code that uses Rational objects """
    pass    

if __name__ == '__main__':
    main()