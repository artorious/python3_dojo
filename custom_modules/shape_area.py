#!/usr/bin/env python3
""" A play at Polymorphism 

NOTE: The word polymorphism derives from Greek meaning “something that takes 
many forms.” In object-oriented programming, polymorphism allows objects of 
different types, each with their own specific behaviors, to be treated as the 
same general type. 
"""

class Shape(object):
    """ Shape class 
    
    All Shape objects have an x, y coordinate (with corresponding getter and 
    setter methods)
    In addition, Shape objects can also calculate their areas.
    How a shape’s area is computed, however, depends on what shape it is. 
    """
    def __init__(self, x_pos, y_pos):
        """ (Shape, int, int) -> Shape

        Initialize <x_pos>, <y_pos> coordinates
        """
        self.__x_pos = x_pos 
        self.__y_pos = y_pos

    def get_xy_loc(self):
        """ (Shape) ->  tuple
        
        Returns  (<x_pos>, <y_pos>) coordinates
        """
        return (self.__x_pos, self.__y_pos)

    def calc_area(self):
        """
        calculate shape area
        """
        raise NotImplementedError('Method calc_area not implemented')