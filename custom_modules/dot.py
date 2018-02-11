#!/usr/bin/env python3
""" A simple graphical object

Derives the Dot class from GraphicalObject and overrides the draw method to
simply draw a red circle within the window.
"""
from graphical_object import GraphicalObject

class Dot(GraphicalObject):
    """ A simple, round circle graphical object """
    
    def __init__(self, **kwargs):
        """ 
        Inits a dot object with a given Turtle screen, pen, and
        (x, y) coordinates
        """
        super().__init__(**kwargs)   # Explicitly invoke superclass constructor
    
    def draw(self):
        """ Renders the dot in the Turtle graphics window """
        self.turtle.penup()     # Move pen
        self.turtle.setpos(self.x_pos, self.y_pos)
        self.turtle.pendown()
        self.turtle.fillcolor("red")
        self.turtle.begin_fill()
        self.turtle.circle(20)
        self.turtle.end_fill()

if __name__ == '__main__':
    # Test Dot class
    from turtle import Screen, Turtle
    # Make a Dot object
    d_obj = Dot(screen=Screen(), turtle=Turtle(), x_pos=10, y_pos=20)
    # Run the graphical program
    d_obj.run()