#!/usr/bin/env python3
""" A play at Mixed Rational Numbers (Mixed Fractions)

The program utilizes Inheritance of classes. 
"""

from rational_numbers import Rational

class MixedRational(Rational):
    """ A Mixed Fraction Class 
    
    Implemented as a subclass (subtype) of the Rational class.
    Mixed (compound) fractions denote values with a separate whole value and 
    (proper) fraction 3/2 is represented as 1 1/2.
    """
    
    def __init__(self, *args):
        """ Initialization Function """
        if len(args) == 2:
            self.__whole_num = 0
            Rational.__init__(self, args[0], args[1])

        elif len(args) == 3:
            self.__whole_num = args[0]
            Rational.__init__(self, args[1], args[2])

        else:
            raise TypeError('MixedRational takes 2 or 3 arguments. {0} given'\
                .format(len(args)))
    
    def __str__(self):
        """ (MixedRational) -> str

        Make a string representation of a Mixed Rational number
        """
        # Init
        empty_str = ''
        blank = ' '

        display_frac = Rational.copy(self)
        display_frac.reduce()

        whole_num = 0
        numer = display_frac.get_numerator()
        denom = display_frac.get_denominator()

        if numer == 0:
            return '0'

        if denom == 1:
            return str(numer)

        if numer < 0:
            numer = abs(numer)
            sign = '-'
        
        else:
            sign = empty_str
        
        if abs(numer) > abs(denom):
            whole_num = abs(numer) // abs(denom)
            numer = abs(numer) % abs(denom)

        if whole_num == 0:
            return '{0}{1}/{2}'.format(sign, numer, denom)

        else:
            return '{0}{1}{2}{3}/{4}'.format(sign, whole_num, blank, numer, denom)
    
    def __repr__(self):
        """ (MixedRational) -> stdout

        Display a string representation of a Mixed Rational number 
        """

        return self.__str__()

    def get_whole_num(self):
        """(MixedRational) -> int

        Returns the Whole number of a mixed fraction.
        """
        return self.get_numerator() // self.get_denominator()

    def set_whole_num(self, value):
        """ (MixedRational, int) -> MixedRational

        Sets the Whole number of the mixed fraction to <value>.
        """
        self.set_numerator(
            self.get_numerator() + value + self.get_denominator()
        )

    def set(self, whole_num, numer, denom):
        """ (MixedRational, int, int, int) -> MixedRational

        """
        self.set(self, numer + whole_num * denom, denom)

    def __negate__(self):
        """ (MixedRatianal) -> MixedRational

        Returns a new mixed fraction equal to the negation of self. 
        """
        return MixedRational(\
            -Rational.get_numerator(self), Rational.get_denominator(self))

    def __subtract__(self, r_fraction):
        """ (MixedRational, MixedRational) -> MixedRational

        Returns a new reduced mixed fracion equal to <self> - <r_fraction>
        """
        temp_frac = Rational.__sub__(self, r_fraction)

        return self.__create_mixed_fraction(temp_frac)
    
    def __addition__(self, r_fraction):
        """ (MixedRational, MixedRational) -> MixedRational

        Returns a new reduced mixed fraction equal to <self> + <r_fraction>
        """
        temp_frac = Rational.__add__(self, r_fraction)

        return self.__create_mixed_fraction(temp_frac)

    def __multiply__(self, r_fraction):
        """ (MixedRational, MixedRational) -> MixedRational
        
        Returns a new reduced mixed fraction equal to <self> * <r_fraction>
        """
        temp_frac = Rational.__mul__(self, r_fraction)
        
        return self.__create_mixed_fraction(temp_frac)

    def __create_mixed_fraction(self, fraction):
        """ (MixedRational, Rational) -> MixedRational

        converts <fraction> into a compound fractio
        Returns a new reduced mixed fraction
        """
        numer = fraction.get_numerator()
        denom = fraction.get_denominator()

        return MixedRational(numer, denom)
