#!/usr/bin/env python3
""" A play at Koch Fractals """

import turtle

def koch(t, order, size):
    """ (Turtle, int, int) -> turtle

    Make turtle <t> draw a koch fractal of <order> and <size>.
    Leave the turtle facing the same direction.
    """
    if order == 0:  # Base case (just a straight line)
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order - 1, size / 3)    # Go 1/3 of the way
            t.left(angle)
def main():
    
    turtle.setup(800, 600) # Set window size
    the_turtle = turtle.getturtle() # Get the (default) turtle
    
    # Set the order
    order = 5
    size = 250

    koch(the_turtle, order, size)

if __name__ == '__main__':
    main()