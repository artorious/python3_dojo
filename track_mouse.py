#!/usr/bin/env
""" A graphical program that responds to mouse clicks and key presses"""

import turtle


def report_mouse_position(x_pos=0, y_pos=0):
    """ (int, int) -> str
    Prints the values of <x_pos> and <y_pos> 
    """
    print('x-axis:', x_pos, ' Y-axis: ', y_pos, flush=True)


if __name__ == '__main__':
    
    # A function that accept a function as a parameter

    # Establish a function the framework should call when the user clicks the mouse
    turtle.onscreenclick(report_mouse_position)

    # Start the graphics loop that listens for user input
    turtle.mainloop()
