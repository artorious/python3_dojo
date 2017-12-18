#!/usr/bin/env
'''Turtle Graphics Example Templates'''

import turtle


def polygon(sides, length, x_pos, y_pos, color, fill=False):
    '''Draw a regular polygon with the given number of <sides>
    of <length>. Pen begins at point(<x_pos>, <y_pos>) and is <color>
    <fill>, default False, fills the polygon with the specifed <color>
    '''
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

