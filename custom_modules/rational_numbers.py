#!/usr/bin/env python3
""" A play at Rational numbers (Fractions)

Uses the Python’s dunder notation to better protect instance variables.

NOTE: 
    This form of protection (information hiding) defends against a 
    conscientious but careless programmer but not a malicious one.
"""

class Rational(object):
    """Represents a rational number (fraction)

    Represents values as common fractions, that is, with just a numerator 
    and denominator. Thus, the value one and a half is represented as 3/2.

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
            raise ValueError('DivisionByZeroError: 0 can\'t be a denominator')

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
        """ (Rational) -> Rational
        
        Simplify Fraction 
        """
        gcd = self.__calc_gcd()
        self.__numerator = self.__numerator // gcd
        self.__denominator = self.__denominator // gcd

    def __calc_gcd(self):
        """ (Rational) -> int
        
        Calculates GCD 
        """
        a = max(self.__numerator, self.__denominator)
        b = min(self.__numerator, self.__denominator)

        while b != 0:
            temp = b
            b = a % b
            a = temp

        return a 

    def __repr__(self):
        """ (Rational) -> stdout

        Make a string representation of a Rational number x/y
        """
        return '{0}/{1}'.format(self.__numerator, self.__denominator)

    def __neg__(self):
        """ (Ratianal) -> Rational

        Returns a new fraction equal to the negation of self. 
        """
        return Rational(-self.__numerator, self.__denominator)

    def __add__(self, r_fraction):
        """ (Rational, Rational) -> Rational

        Returns a new reduced fraction equal to <self> + <r_fraction>
        """
        numer = self.__numerator * r_fraction.get_denominator() +\
                r_fraction.get_numerator() * self.__denominator

        denom = self.__denominator * r_fraction.get_denominator()

        result_addition = Rational(numer, denom)
        result_addition.reduce()

        return result_addition
    
    def __sub__(self, r_fraction):
        """ (Rational, Rational) -> Rational

        Returns a new reduced fracion equal to <self> - <r_fraction>
        """

        return self + (-r_fraction)

    def __multiply__(self, r_fraction):
        """ (Rational, Rational) -> Rational
        
        Returns a new reduced fraction equal to <self> * <r_fraction>
        """
        numer = self.__numerator * r_fraction.get_numerator()
        denom = self.__denominator * r_fraction.get_denominator()

        result_multiply = Rational(numer, denom)

        result_multiply.reduce()

        return result_multiply
    
    def copy(self):
        """ (Rational, Rational) -> Rational

        Make a copy of the fraction 
        """
        new_frac = Rational(self.__numerator, self.__denominator)
        return new_frac

    def __adjust(self, factor):
        """ (Rational, int) -> Rational
        
        Adjust fraction by <factor>
        """
        self.set_numerator(self.get_numerator() * factor)
        self.set_denominator(self.get_denominator() * factor)

    def __eq__(self, r_fraction):
        """ (Rational, Rational) -> bool
        
        Returns True if <self> arithmetically equal to <r_fraction>
        otherwise, returns False
        """
        temp_frac1 = self.copy()
        temp_frac2 = r_fraction.copy()
        temp_frac1.reduce()
        temp_frac2.reduce()

        if temp_frac1.get_numerator() == temp_frac2.get_numerator() and \
           temp_frac1.get_denominator() == temp_frac2.get_denominator():
            return True
        else:
            return False
    
    def __neq__(self, r_fraction):
        """(Rational, Rational) -> bool
        
        Returns True if <self> is NOT arithmetically equal to <r_fraction>
        otherwise, returns False
        """
        return not self.__eq__(r_fraction)

    def __lt__(self, r_fraction):
        """(Rational, Rational) -> bool
        
        Returns True if <self> is less than <r_fraction>
        """
        if self.get_denominator() == r_fraction.get_denominator:
            return self.get_numerator() < r_fraction.get_numerator()
        else:
            temp_frac1 = self.copy()
            temp_frac2 = r_fraction.copy()

            saved_denom = temp_frac1.get_denominator()
            temp_frac1.__adjust(temp_frac2.get_denominator())
            temp_frac2.__adjust(saved_denom)

            return temp_frac1.get_numerator() < temp_frac2.get_numerator()

    def __le__(self, r_fraction):
        """(Rational, Rational) -> bool
        
        Returns True if <self> is less than or equal to <r_fraction>
        """
        if self == r_fraction or self < r_fraction:
            return True
        else:
            return False

    def __gt__(self, r_fraction):
        """(Rational, Rational) -> bool
        
        Returns True if <self> is greater than <r_fraction>
        """
        if not(self <= r_fraction):
            return True
        else:
            return False

    def __ge__(self, r_fraction):
        """(Rational, Rational) -> bool
        
        Returns True if <self> is greater than or equal to <r_fraction>
        """
        if not(self < r_fraction):
            return True
        else:
            return False


def main():
    """ Client code that uses Rational objects """
    fract1 = Rational(1, 2)
    fract2 = Rational(1, 4)
    fract3 = Rational(2, 4)

    print('Arithmetic operations on Fractions; {0}, {1} and {2}'.format(
        fract1, fract2, fract3))
    print()
    print('{0} * {1} = {2}'.format(
        fract1, fract2, fract1.__multiply__(fract2)))
    print('{0} + {1} = {2}'.format(
        fract1, fract2, fract1.__add__(fract2)))
    print('{0} - {1} = {2}'.format(
        fract1, fract2, fract1.__sub__(fract2)))

    print('Negate({0}) = {1}'.format(fract1, fract1.__neg__()))
    print('Negate({0}) = {1}'.format(fract2, fract2.__neg__()))
    
    print()
    print('Relational operations on Fractions; {0}, {1} and {2}'.format(
            fract1, fract2, fract3))
    print()
    print('{0} is equal to {1} : {2}'.format(
        fract1, fract2, fract1.__eq__(fract2)))
    print('{0} is equal to {1} : {2}'.format(
        fract3, fract1, fract3.__eq__(fract1)))
    print('{0} is equal to {1} : {2}'.format(
        fract2, fract3, fract2.__eq__(fract3)))

    print('{0} is NOT equal to {1} : {2}'.format(
        fract1, fract2, fract1.__neq__(fract2)))
    print('{0} is NOT equal to {1} : {2}'.format(
        fract3, fract1, fract3.__neq__(fract1)))

    print('{1} is less than {0} : {2}'.format(
        fract1, fract2, fract2.__lt__(fract1)))
    print('{0} is less than {1} : {2}'.format(
        fract3, fract1, fract3.__lt__(fract1)))

    print('{1} is less or equal to {0} : {2}'.format(
        fract1, fract2, fract2.__lt__(fract1)))

    print('{1} is greater than {0} : {2}'.format(
        fract1, fract2, fract2.__gt__(fract1)))
    print('{0} is greater than {1} : {2}'.format(
        fract3, fract1, fract3.__gt__(fract1)))

    print('{1} is greater than or equal to {0} : {2}'.format(
        fract1, fract2, fract2.__ge__(fract1)))
    print('{0} is greater than or equal to {1} : {2}'.format(
        fract3, fract1, fract3.__ge__(fract1)))
    print()
        
    fract1.set_numerator(3)
    fract1.set_denominator(4)
    fract2.set_numerator(2)
    fract2.set_denominator(3)

    print('Arithmetic operations on Fractions; {0} and {1}'.format(
        fract1, fract2))
    print()
    print('{0} * {1} = {2}'.format(
        fract1, fract2, Rational.__multiply__(fract1, fract2)))
    print('{0} + {1} = {2}'.format(
        fract1, fract2, Rational.__add__(fract1, fract2)))
    print('{0} - {1} = {2}'.format(
        fract1, fract2, Rational.__sub__(fract1, fract2)))

    print('Negate({0}) = {1}'.format(fract1, Rational.__neg__(fract1)))
    print()
    
    print('Relational operations on Fractions; {0} and {1}'.format(
        fract1, fract2))
    print()
    print('{0} is equal to {1} : {2}'.format(
        fract1, fract2, Rational.__eq__(fract1, fract2)))

    print('{0} is NOT equal to {1} : {2}'.format(
        fract1, fract2, Rational.__neq__(fract1, fract2)))

    print('{0} is less than {1} : {2}'.format(
        fract1, fract2, Rational.__lt__(fract1, fract2)))

    print('{0} is less or equal to {1} : {2}'.format(
        fract1, fract2, Rational.__le__(fract1, fract2)))

    print('{0} is greater than {1} : {2}'.format(
        fract1, fract2, Rational.__gt__(fract1, fract2)))
    print('{0} is greater than or equal to {1} : {2}'.format(
        fract1, fract2, Rational.__ge__(fract1, fract2)))

    # fract_bad = Rational(4, 0)

if __name__ == '__main__':
    main()