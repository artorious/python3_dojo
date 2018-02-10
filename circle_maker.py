#!/usr/bin/env python3
""" Use Turtle graphics to render Circle objects in a graphical window.

An interactive program that allows the user to place the image of a Circle
object in the window via a mouse click.
Susequent mouse clicks move the circle to the mouse position.
Users can us the <Up> and <Down> cursor keys to enlarge and reduce the size
of the circle.
"""

from turtle import Turtle, Screen, mainloop
from custom_modules.circle import Circle

class GraphicalCircle(object):
    """
    Wraps Circle object with a primitive graphical interface.
    Each GraphicalCircle object maintains its own circle object
    and Turtle graphics Turtle object.
    """
    def __init__(self, center, radius):
        """ (GraphicalCircle, tuple, int) -> GraphicalCircle
        
        Initializes a graphical circle object 
        The circle is centered at the position <center>.
        The circle radius is set to the <radius>
        """
        # Make a turtle graphics object to do the drawing.
        # Assign it to an instance variable the_turtle, 
        # so other methods can access it
        self.the_turtle = Turtle()
        self.the_turtle.speed(0)            # fastest turtle
        self.the_turtle.hideturtle()        # hide turtle
        the_screen = Screen()               # Create local screen object: Receive user input
        the_screen.delay(0)                 # trace drawing delay - slow
        the_screen.listen()                 # focus on keystrokes
        # Mouse click re-positions the circle
        the_screen.onclick(self.move)       # Set mouse press handler - 
        # Up cursor key calls the increases method to expand the circle
        the_screen.onkey(self.increase, 'Up')       # Set "up" cursor key handler
        # Down cursor key calls the deecrease method to contract the circle
        the_screen.onkey(self.decrease, 'Down')     # Set "Down" cursor key handler
        
        # Make a circle object
        # Assign it to an instance variable the_circle, 
        # so other methods can access it
        self.the_circle = Circle(center, radius)
        mainloop()      # Start event loop
    
    def draw(self):
        """ (GraphicalCircle) -> turtle
        Draw circle in the graphical window
        """
        x_pos, y_pos = self.the_circle.get_center()         # unpack center's coordinates
        radius = self.the_circle.get_radius()
        self.the_turtle.penup()                             # lift pen
        self.the_turtle.setposition(x_pos, y_pos)           # Move pen to (x,y) position
        self.the_turtle.pendown()                           # pen ready
        self.the_turtle.dot()                               # draw dot: circle's center
        self.the_turtle.penup()                             # lift pen
        self.the_turtle.setposition(x_pos, y_pos - radius)  # position pen to draw rim of circel
        self.the_turtle.pendown()                           # pen ready
        self.the_turtle.circle(radius)                      # draw the circle
        self.the_turtle.penup()                             # lift pen

    def move(self, x_pos, y_pos):
        """ (int, int) -> turtle 

        Moves the circle's center to <x_pos> and <y_pos>
        Delegates the work to the contained Circle object
        """
        self.the_circle.move((x_pos,y_pos)) # Move to new pos
        self.redraw()

    def increase(self):
        """ (GraphicalCircle) -> turtle
        
        Increase the circle's radius by 1 unit, then redraw the circle
        Delegates the work to the contained Circle object
        """
        self.the_circle.grow()
        self.redraw()

    def decrease(self):
        """ (GraphicalCircle) -> turtle
        
        Decrease the circle's radius by 1 unit, then redraw the circle
        Delegates the work to the contained Circle object
        """
        self.the_circle.shrink()
        self.redraw()

    def redraw(self):
        """ (GraphicalCircle) -> turtle
        Clears the graphical window, then draws the circle
        """
        self.the_turtle.clear()
        self.draw()

def main():
    """Allows the user to manipulate a graphical circle object"""
     
    the_circle = GraphicalCircle((0, 0), 100) # Make a graphical circle object
    print("Program done")

if __name__ == '__main__':
    main()




