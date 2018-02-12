#!/usr/bin/env python3
""" Draw boxes on a turtle screen

NOTE:
    Use with box_adapter.py
"""

class Box(object):
    """ A square box object """

    def __init__(self, screen, pen, x_pos, y_pos, width):
        """
        Ininitializes a box object with a given Turtle <screen>, <pen>, 
        (x_pos, y_pos) position, and width
        """
        self._screen = screen
        self._pen = pen
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._width = width
    
    def position(self, x_pos, y_pos):
        """
        Positions the box at (x_pos, y_pos)
        """
        self._x_pos = x_pos
        self._y_pos = y_pos
    
    def render(self):
        """
        Renders the box in the Turtle graphics window
        """
        self._pen.penup()   # Move pen
        self._pen.setpos(self._x_pos - self._width / 2, 
                        self._y_pos - self._width / 2)
        self._pen.setheading(0)
        self._pen.pendown()
        self._pen.fillcolor('blue')
        self._pen.begin_fill()
        self._pen.forward(self._width)
        self._pen.left(90)
        self._pen.forward(self._width)
        self._pen.left(90)
        self._pen.forward(self._width)
        self._pen.left(90)
        self._pen.forward(self._width)
        self._pen.left(90)
        self._pen.endfill()
        