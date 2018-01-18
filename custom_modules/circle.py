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
        """ (Circle, tuple, float) -> Init

        Initialize instance variables
        The Circle's center's <center> and <radius>;
        negative radius not accepted
        """
        pass
    
    def get_radius(self):
        """ (Circle) -> float 
        
        Return the radius of the circle 
        """
        return

    def get_center(self):
        """ (Circle) -> tuple 
        
        Return the coordinates of the center
        """
        return 

    def get_area(self):     
        """ (Circle) -> float
        Compute and Return the area of the circle
        """
        return
    
    def get_circumference(self):
        """ (Circle) -> float
        Compute and Return the circumference of the circle
        """
        return
    
    def move(self, new_pos):
        """ (Circle, tuple) -> variable re-assignment
        
        Moves the center of the circle to point <new_pos>
        """
        pass
    
    def grow(self):
        """ (Circle) -> variable re-assignment

        Increases the radius of the circle
        """
        pass

    def shrink(self):
        """ (Circle) -> variable re-assignment

        Decreases the radius of the circle;
        does not affect a circle with radius zero
        """
        pass
