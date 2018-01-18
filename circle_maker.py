#!/usr/bin/env python3
""" Use Turtle graphics to render Circle objects in a graphical window.

An interactive program that allows the user to place the image of a Circle
object in the window via a mouse click. 
Susequent mouse clicks move the circle to the mouse position. 
Users can us the <Up> and <Down> cursor keys to enlarge and reduce the size 
of the circle. 
"""

from turtle import Turtle, Screen, mainloop, delay, clear
from custom_modules.circle import Circle

the_turtle = Turtle()   # Global turtle
the_circle = Circle((0, 0), 100)   # Global circle object

def draw_circle(a_turtle, a_circle):
    """ (Turtle, Circle) -> turtle
    
    Draw circle in the graphical window
    """

    pass

def do_click(x_pos, y_pos):
    """ (int, int) -> turtle 
    
    Moves circle. packs up into a tuple the x and y coordinates it receives 
    passes this tuple on to the global Circle object circ’s move method.
    """
    pass

def do_up():
    """
    Enlarge
    """
    pass

def do_down():
    """
    Make smaller
    """
    pass

def redraw():
    """
    Clear and draw again
    """
    pass

def main():
    """Use Turtle graphics to render Circle objects in a graphical window."""
    delay(0)                    # trace drawing delay - slow
    the_turtle.speed(0)         # fastest turtle
    the_turtle.hideturtle()     # hide turtle 
    the_screen = Screen()       # Create screen object: Receive user input
    the_screen.listen()         # focus on keystrokes
    
    
    the_screen.onclick(do_click)    # Set mouse press handler - 
    the_screen.onkey(do_up, 'Up')   # Set "up" cursor key handler
    the_screen.onkey(do_down, 'Down')   # Set "Down" cursor key handler
    mainloop()      # Start event loop     

if __name__ == '__main__':
    main()