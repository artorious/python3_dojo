#!/usr/bin/env
""" Turtle Graphics Example Templates """

import turtle

def polygon(sides, length, x_pos, y_pos, color, fill=False):
    """ (int, int, int, int, str, bool) -> turtle
    Draw a regular polygon with the given number of <sides>
    of <length>. Pen begins at point(<x_pos>, <y_pos>) and is <color>
    <fill>, default False, fills the polygon with the specifed <color>
    """

    try:
        turtle.bgcolor('black')
        turtle.penup()
        turtle.setposition(x_pos, y_pos)
        turtle.pendown()
        turtle.color(color)
        if fill:
            turtle.begin_fill()
        
        for poly_sides in range(sides):
            turtle.forward(length)
            turtle.left(360 // sides)
        if fill:
            turtle.end_fill()

    except TypeError as err1:
        return err1
    except Exception as err2: # Handle TurtleGraphicsError
        return err2

    
def draw_horizontal_lines(how_many, length, y_pos, color):
    """ (int, int, int, str) -> turtle
    Draws <how_many> <color> horizontal lines of <length> stacked on top
    of each other with the lowest line appearing at position <y_pos> on the 
    y-axis . 
    """
    try:
        turtle.color(color)
        for line in range(how_many):
            turtle.penup()
            turtle.setposition(-200, y_pos)
            turtle.pendown()
            turtle.forward(length)
            y_pos += 10

    except TypeError as err1:
        return err1
    except Exception as err2: # Handle TurtleGraphicsError
        return err2
