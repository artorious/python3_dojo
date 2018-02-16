#!/usr/bin/env python3
""" Sierpinski Triangle Program (Fractals)

A turtle graphics program that generates Sierpinski triangles at various 
levels of repetition.This program utilizes recursive functions

NOTE:
    The Sierpinski triangle is an example of a fractal. A fractal is a shape 
    that contains parts that are similar to the whole shape, thus having the 
    property of self-similarity 
"""

import turtle
from math import sqrt # calculation of the height of a triangle

# NOTE:
#   In the Sierpinski triangle, each next level in the pattern replaces each
#   triangle with three smaller triangles.  
# In order for the position of each next triangle to be determined by functions: 
# get_left_triangle_position, get_right_triangle_position,get_top_triangle_position 
# respectively, both the length of the sides of the triangle, as well as its 
# height are needed.

def create_triangle_shape(coords):
    """ (tuple, tuple, tuple) -> turtle
    
    Creates turtle shape from <coords>.
    Registers shape as 'my_triangle'.
    """
    turtle.penup()
    turtle.begin_poly()
    turtle.setposition(coords[0])
    turtle.setposition(coords[1])
    turtle.setposition(coords[2])
    turtle.setposition(coords[0])
    turtle.end_poly()

    tri_shape = turtle.get_poly()
    turtle.register_shape('my_triangle', tri_shape)

def triangle_height(side):
    """ (float) -> float

    Returns height of equilateral triangle with length <side>
    """
    return sqrt(3) / 2 * side 

 
    # The position of turtle shapes in turtle graphics is relative to the center 
    # of the shape. Each triangle is positioned relative to its center point 
    # Thus, method get_left_triangle_position calculates the location of the 
    # bottom left triangle as,

    #   [position [0] - side / 4, position [1] - triangle_height(side) / 4]

    # As a result, the x (horizontal) position of the lower left triangle is one 
    # quarter of the length of the side less than the larger triangle, therefore 
    # positioned to the left of the larger triangle’s location. 
    # 
    # The y (vertical) position of the smaller triangle is one quarter of the 
    # height of the triangle less than the larger triangle, thus placed below 
    # the position of the original triangle. 

def get_left_triangle_position(position, side):
    """ (tuple, float) -> tuple
    
    Returns position of bottom left triangle in larger triangle.
    Returns (x, y) position for provided <position> and <side> length of 
    larger trinagle to be placed within
    """
    return (position[0] - side / 4, position[1] - triangle_height(side) / 4)

    # Positioning of the lower right triangle (by method 
    # get_right_triangle_position) is similarly determined (positioned to the 
    # right of and below the location of the original triangle). 

def get_right_triangle_position(position, side):
    """ (tuple, float) -> tuple

    Returns position of bottom right triangle in larger triangle.
    Returns (x, y) position for provided <position> and <side> length of 
    larger trinagle to be placed within
    """
    return (position[0] + side / 4, position[1] - triangle_height(side) / 4)

    # Finally, method get_top_triangle_position determines the position of the 
    # smaller top triangle to be at the same x location as the original triangle, 
    # and one quarter of the height of the triangle higher.

def get_top_triangle_position(position, side):
    """ (tuple, float) -> tuple

    Returns x,y position of top triangle within larger one.
    For triangle at <position> with length <side>
    """
    return (position[0], position[1] + triangle_height(side) / 4)

def draw_sierpinski_triangle(t, len_side, levels):
    """ (Turtle, float, int) -> turtle

    Recursive function that draws a Sierpinski triangle, for parameters;
    the turtle <t>, with <ln_side> length of the sides of the overall 
    triangle, number of <levels> of the Sierpinski triangle pattern to draw.
    """
    # base case in which the function no longer calls itself.
    if levels == 0:
        t.color('black')    # Display triangle
        t.showturtle()
        t.stamp()

        return

    # Resize triangle to half it's size
    stretch_width, stretch_length, outline = t.turtlesize()
    t.turtlesize(0.5 * stretch_width, 0.5 * stretch_length, outline)

    # Determine position for each of the three embedded triangles
    left_triangle_position = get_left_triangle_position(
        t.position(), len_side)
    right_triangle_position = get_right_triangle_position(
        t.position(), len_side)
    top_triangle_position = get_top_triangle_position(
        t.position(), len_side)

    # recursively display the left triangle
    t.setposition(left_triangle_position)
    draw_sierpinski_triangle(t, len_side / 2 , levels -1)
    t.turtlesize(0.5 * stretch_width, 0.5 * stretch_length, outline)

    # recursively display the right triangle
    t.setposition(right_triangle_position)
    draw_sierpinski_triangle(t, len_side / 2 , levels -1)
    t.turtlesize(0.5 * stretch_width, 0.5 * stretch_length, outline)

    # recursively display the left triangle
    t.setposition(top_triangle_position)
    draw_sierpinski_triangle(t, len_side / 2 , levels -1)
    t.turtlesize(0.5 * stretch_width, 0.5 * stretch_length, outline)

def main():
    """Fractals - Sierpinski Triangle Program 
    
    Does the needed preparation before drawing can begin.

    """
    turtle.setup(800, 600) # Set window size

    the_turtle = turtle.getturtle() # Get the (default) turtle
    
    # Init turtle: drawing capability(off) and hidden
    # only graphics to be produced by the turtle is when its (triangle) shape is stamped.
    the_turtle.penup()
    the_turtle.hideturtle()
    
    # Set number of levels: 
    # by changing this value, a Sierpinski triangle of various levels can be 
    # created.
    num_levels = 2

    # Create triangle shape
    # a tuple of coordinates that creates an equilateral triangle. 
    # (The absolute positions of these coordinates are not relevant, only their 
    # relative positions are used for defining the shape.)
    coords = ((-240, -150), (240, -150), (0, 266)) 
    create_triangle_shape(coords)
    # length of the triangle, matching the length of the triangle given by the specified coordinates.
    len_side = 480 

    # create first triangle
    the_turtle.shape('my_triangle') # set to shape (register)
    the_turtle.setposition(0, -50) #  position on screen (a little below the center)
    the_turtle.setheading(90)   #  ensure that the triangle is pointing up

    # call recursive function
    draw_sierpinski_triangle(the_turtle, len_side, num_levels)
    the_turtle.hideturtle()

    # terminate prog when close window
    turtle.exitonclick()




if __name__ == '__main__':
    main()

