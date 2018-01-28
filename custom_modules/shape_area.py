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
        """ (Shape, int, int) -> float, float

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
        """ (Shape) -> Exception
        Abstract method to handle calculation of shape area
        """
        raise NotImplementedError('Method calc_area not implemented')


class Circle(Shape):
    """
    Subclass of the Shape class implementing the calc_area method,
    for calculating the area of a circle.
    Otherwise NotImplementedError exception is raised
    """
    def __init__(self, x_pos, y_pos, radius):
        """ (Circle, int, int) -> Shape, float

        Initialize Shape object and radius value
        """
        Shape.__init__(self, x_pos, y_pos)
        self.__radius = radius

    def calc_area(self):
        """ (Circle) -> float
        
        Calculate Circle's area
        """
        from math import pi
        return pi * self.__radius ** 2

class Square(Shape):
    """
    Subclass of the Shape class implementing the calc_area method,
    for calculating the area of a square.
    Otherwise NotImplementedError exception is raised
    """
    def __init__(self, x_pos, y_pos, side_len):
        """ (Square, int, int, int) -> Shape, float

        Initialize Shape object and side-length value
        """
        Shape.__init__(self, x_pos,y_pos)
        self.__side_len = side_len
    
    def calc_area(self):
        """ (Circle) -> float
        
        Calculate Square's area
        """
        return self.__side_len ** 2
    

class Triangle(Shape):
    """
    Subclass of the Shape class implementing the calc_area method,
    for calculating the area of an equilateral triangle.
    Otherwise NotImplementedError exception is raised
    """
    def __init__(self, x_pos, y_pos, side_len):
        """ (Triangle, int, int, int) -> Shape, float

        Initialize Shape object and side-length value
        """
        Shape.__init__(self, x_pos, y_pos)
        self.__side_len = side_len
    
    def calc_area(self):
        """ (Triangle) -> float
        
        Calculate Triangle's area
        """
        from math import sqrt
        return (self.__side_len ** 2) * sqrt(3) / 4.0