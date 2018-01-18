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
 
the_turtle = Turtle()   # Init Global turtle
the_circle = Circle((0, 0), 100)   # Init Global circle object

def draw_circle(a_turtle, a_circle):
    """ (Turtle, Circle) -> turtle
    
    Draw circle in the graphical window
    """

    x_pos, y_pos = a_circle.get_center()  # unpack center's coordinates
    radius = a_circle.get_radius()
    a_turtle.penup()                      # lift pen
    a_turtle.setposition(x_pos, y_pos)     # Move pen to (x,y) position
    a_turtle.pendown()                    # pen ready
    a_turtle.dot()                          # draw dot: circle's center
    a_turtle.penup()            # lift pen
    a_turtle.setposition(x_pos, y_pos - radius)     # position pen to draw rim of circel
    a_turtle.pendown()      # pen ready
    a_turtle.circle(radius) # draw the circle
    a_turtle.penup()    # lift pen

def do_click(x_pos, y_pos):
    """ (int, int) -> turtle 
    
    Moves circle. packs up into a tuple the x and y coordinates it receives 
    passes this tuple on to the global Circle object circ’s move method.
    """
    the_circle.move((x_pos,y_pos)) # Move to new pos
    redraw()

def do_up():
    """
    Enlarge
    """
    the_circle.grow()
    redraw()


def do_down():
    """
    Make smaller
    """
    the_circle.shrink()
    redraw()

def redraw():
    """
    Clear and draw again
    """
    the_turtle.clear()
    draw_circle(the_turtle, the_circle)

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