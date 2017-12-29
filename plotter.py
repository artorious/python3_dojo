#!/usr/bin/env python3
""" Provides the plot function that draws the graph of a matehematical
function on a Cartesian coordinate plane.

Combines the concepts of; 
    • lambda functions 
    • functions as data
    • Turtle graphics 
        
"""

import turtle

def initialize_plotter(width, height, min_x, max_x, min_y, max_y):
    """(int, int, int, int, int, int) -> turtle

    Initializes the plotter with a window with dimensions <width> X <height>
    The x-axis ranging from <min_x> to <max_x> and the y-axis ranging from
    <min_y> to <max_y>. 
    Establishes the global beginning and ending x values for the plot and the
    plot and the global x_increment value. 

    Draws an x- and y-axis to simulate a Cartesian coordinate plane. 
    """
    global x_begin, x_end, x_increament # vars accesible to other functions

    # turtle.tracer(1,0)    # Speed up rendering
    turtle.delay(0)     # Speed up rendering
    x_begin, x_end = min_x, max_x   # Est. global x and y ranges
    turtle.setup(width=width, height=height)    # Set up window-size(px)
    turtle.screensize(width, height)    # Set up screen-size(px)
    turtle.setworldcoordinates(min_x, min_y, max_x, max_y)

    # x-axis distance that corresponds to one pixel in window distance
    x_increament = (max_x - min_x) / width  

    turtle.hideturtle()     # Make pen invisible
    # Draw x-axis
    turtle.pencolor('black')
    turtle.penup()
    turtle.setposition(min_x, 0) # Move the pen to the left, center
    turtle.setheading(0) # Aim pen right
    turtle.pendown()
    turtle.forward(max_x - min_x)   # Draw a line left to right

    # Draw y-axis
    turtle.penup()
    turtle. setposition(0, min_y) # Move pen to center, bottom
    turtle.setheading(90) # Aim pen upwards
    turtle.pendown()
    turtle.forward(max_y - min_y) # Draw line bottom to top
    

def plot(math_func, color):
    """(expr, str) -> turtle

    Plots function <math_func> on the Cartesian coordinate plane established
    by initialize_plotter. 
    Plots (x, f(x)), for all x in the range x_begin <= x < x_end
    <color> parameter dictates the curve's color
    """
    pass

def finish_plotting():
    """
    Finishes rendering the Turtle graphics.
    """
    pass

def quad(x):
    """
    Represents the mathematical quadratic function f(x) = ((1/2)x^2) + 3. 
    A caller can pass this to plot()  for rendering.
    """
    return

def test_plotter():
    """ Provides a simple test of the plot function """
    pass

if __name__ == '__main__':
    test_plotter()

