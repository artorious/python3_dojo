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
        pass
    
    def __str__(self):
        """ (MixedRational) -> str

        Make a string representation of a Mixed Rational number
        """
        return
    
    def __repr__(self):
        """ (MixedRational) -> stdout

        Display a string representation of a Mixed Rational number 
        """

        return

    def get_whole_num(self):
        """(MixedRational) -> int

        Returns the Whole number of a mixed fraction.
        """
        return

    def set_whole_num(self, value):
        """ (MixedRational, int) -> MixedRational

        Sets the Whole number of the mixed fraction to <value>.
        """
        return

    def set(self, whole_num, numer, denom):
        """ (MixedRational, int, int, int) -> MixedRational

        """
        return

    def __neg__(self):
        """ (MixedRatianal) -> MixedRational

        Returns a new mixed fraction equal to the negation of self. 
        """
        return

    def __sub__(self, r_fraction):
        """ (MixedRational, MixedRational) -> MixedRational

        Returns a new reduced mixed fracion equal to <self> - <r_fraction>
        """
        return
    
    def __add__(self, r_fraction):
        """ (MixedRational, MixedRational) -> MixedRational

        Returns a new reduced mixed fraction equal to <self> + <r_fraction>
        """
        return

    def __mul__(self, r_fraction):
        """ (MixedRational, MixedRational) -> MixedRational
        
        Returns a new reduced mixed fraction equal to <self> * <r_fraction>
        """
        return

    def __create_mixed_fraction(self, fraction):
        """ (MixedRational, Rational) -> MixedRational

        converts <fraction> into a compound fractio
        Returns a new reduced mixed fraction
        """
        return