#!/usr/bin/env python3
""" A play at Python Custom Types - Circle Objects 

NOTE:
    A software object generally bundles together data (instance variables) 
    and functionality (methods). The instance variables and methods of an 
    object comprise its members. The class of an object defines the object’s 
    basic structure and capabilities.
"""
class Circle():
    """ Represents a geometric circle object """

    def __init__(self, center, radius):
        """ (Circle, tuple, float) -> tuple, float

        Initialize instance variables
        The Circle's center's <center> and <radius>;
        negative radius not accepted
        """
        # Disallow a negative radius
        if radius < 0:
            raise ValueError('Negative radius: NOT VALID')

        self.center = center
        self.radius = radius
    
    def get_radius(self):
        """ (Circle) -> float 
        
        Return the radius of the circle 
        """
        return self.radius

    def get_center(self):
        """ (Circle) -> tuple 
        
        Return the coordinates of the center
        """
        return self.center

    def get_area(self):     
        """ (Circle) -> float
        
        Compute and Return the area of the circle
        """
        from math import pi
        return pi * self.radius * self.radius
    
    def get_circumference(self):
        """ (Circle) -> float
        
        Compute and Return the circumference of the circle
        """
        from math import pi
        return 2 * pi * self.radius
    
    def move(self, new_pos):
        """ (Circle, tuple) -> tuple
        
        Moves the center of the circle to point <new_pos>
        performs variable re-assignment
        """
        self.center = new_pos
    
    def grow(self):
        """ (Circle) -> float

        Increases the radius of the circle
        performs variable re-assignment
        """
        self.radius += 1

    def shrink(self):
        """ (Circle) -> float

        Decreases the radius of the circle;
        does not affect a circle with radius zero
        performs variable re-assignment
        """
        if self.radius > 0:
            self.radius -= 1
