#!/usr/bin/env python3
""" A play at Polymorphism 

NOTE: The word polymorphism derives from Greek meaning “something that takes 
many forms.” In object-oriented programming, polymorphism allows objects of 
different types, each with their own specific behaviors, to be treated as the 
same general type. 
"""
class Bird(object):
    """ Abstaract Class """
    def __init__(self, weight):
        """ (Bird, float) -> stdout, Bird
        Init 
        """
        print('__init__ of Bird class called.')
        self.__weight = weight
    
    def get_weight(self):
        """ (Bird) -> str
        Return Bird object weight
        """
        return '{0} ounces'.format(self.__weight)

    def get_color(self):
        """ (Bird) -> Exception
        Abstract Method
        """
        raise NotImplementedError('Method color not Implemented')

class BlueJay(Bird):
    """ Subclass of Bird class """
    def __init__(self, weight):
        """ (BlueJay, float) -> Bird
        Init 
        """
        Bird.__init__(self, weight)
    
    def get_color(self):
        """ (BlueJay) -> str 
        Returns Bird's color
        """
        return 'Blue'

class Cardinal(Bird):
    """ Subclass of Bird class """
    def __init__(self, weight):
        """ (Cardinal, float) -> Bird
        Init 
        """
        Bird.__init__(self, weight)
    
    def get_color(self):
        """ (Cardinal) -> str 
        Returns Bird's color
        """
        return 'Red'

class BlackBird(Bird):
    """ Subclass of Bird class """
    def __init__(self, weight):
        """ (BlackBird, float) -> Bird
        Init 
        """
        Bird.__init__(self, weight)
    
    def get_color(self):
        """ (BlackBird) -> str 
        Returns Bird's color
        """
        return 'Black'
