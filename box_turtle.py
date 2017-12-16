#!/usr/bin/env
'''Turle Graphics Examples'''

import turtle
import random

def polygon(sides, length, x_pos, y_pos, color):
    '''Draw a regular polygon with the given number of <sides>
    of <length>. Pen begins at point(<x_pos>, <y_pos>) and is <color>
    '''
    turtle.bgcolor('black')
    turtle.penup()
    turtle.setposition(x_pos, y_pos)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    
    for poly_sides in range(sides):
        turtle.forward(length)
        turtle.left(360 // sides)
    turtle.end_fill()

# Disable rendering to speed up drawing
turtle.hideturtle()
turtle.tracer(0)

#### Draw random polygons
for a_polygon in range(20): # 20 polygons
    polygon(
        random.randrange(3, 11),        # 3-11 sides
        random.randrange(10, 51),       # length ranges
        random.randrange(-250, 251),    # x-axis position ranges
        random.randrange(-250, 251),    # y-axis position ranges
        random.choice(('red', 'lime', 'cyan', 'yellow', 'purple'))  # Select color at random from tuple
    )
turtle.update() # Render image
turtle.exitonclick() # mouse click to exit