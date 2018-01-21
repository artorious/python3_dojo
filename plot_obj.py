#!/usr/bin/env python3
""" Plotting Data

Provides the Plotter class that clients can use to draw graphs
of a mathematical functions on a Cartesian coordinate plane.

TODO:
Test code using the unittest module in the Python standard library.
Use Turtle graphics to plot mathematical functions. 
Use a class to wrap the details of Turtle graphics and design a plotter
object that is more convenient for programmers. 
Enable plotting of data obtained experimentally.
"""

from turtle import Pen, Screen
from math import atan2, pi

class Plotter(object):
    """
    A plotter object provides a graphical window for plotting data and 
    mathematical functions.
    """

    def __init__(self, width, height, min_x, max_x, min_y, max_y):
        """ (Plotter, int, int, int, int, int, int) -> turtle
        
        The constructor initializes the Turtle graphics window. 
        It accepts parameters that define the window’s physical size and 
        ranges of x and y axes.

        Initializes the plotter with a window that is <width> wide and 
        <height> high. Its x-axis ranges from <min_x> to <max_x>, and it's 
        y-axis ranges from <min_y> to <max_y>.

        Establishes the global begining and ending x values for the plot and
        the x_increament value.
        Draws the x-axis and y-axes
        """
        # Init
        self.pen = Pen()    # The plotter object's pen
        self.screen = Screen() # The plotter object's sceen

        self.pen.speed(0)   # Speed up rendering
        self.screen.tracer(0, 0) # DONT draw pen while drawing

        # Establish global x and y ranges
        self.min_x, self.max_x = min_x, max_x
        self.min_y, self.max_y = min_y, max_y

        self.screen.setup(width=width, height=height) # Set up window size, in pixels

        # set up screen size, in pixels
        self.screen.screensize(width, height)
        self.screen.setworldcoordinates(min_x, min_y, max_x, max_y)

        # x-axis distance that correspond to one pixel in window distance
        self.x_increament = (max_x - min_x) / width
        self.draw_grid(20)
        self.draw_axes()
        self.screen.title('Plot')
        self.screen.update()

    def __del__(self): 
        """ (Plotter) -> stdout

        Called when the client no longer uses the plotter object. 

        The interpreter calls this method, also known as destructor, 
        when the object is no longer bound to a reference with in the 
        executing program. 
        Among other times, this happens when the program’s execution 
        terminates.
        """
        print('Done Printing')

    def draw_axes(self, grid=False):
        """ (Plotter, bool) -> turtle

        Draws the x and y axes within the plotting window.

        An option Boolean parameter <grid> controls the drawing of
        accessory horizontal and vertical lines
        """
        if grid:
            self.draw_grid(20)
        self.pen.hideturtle()   # Make pen invisible
        prev_width = self.pen.width()
        self.pen.width(2)

        # Draw x axis
        self.pen.color('black')
        self.draw_arrow(self.min_x, 0, self.max_x, 0)

        # Draw y axis
        self.draw_arrow(0, self.min_y, 0, self.max_y)
        self.pen.width(prev_width)
        
    def draw_grid(self, num):
        """ (Plotter, int) -> turtle

        Draws horizontal and vertical accessory reference coordinate 
        lines on the plot. Parameter <num> control the frequency of the 
        reference lines.
        """
        self.pen.up()
        # self.pen.setposition(self.min_x, self.min_y)
        inc = (self.max_x - self.min_y) / num
        self.pen.color('lightblue')
        x = self.min_x

        while x <= self.max_x:
            self.pen.setposition(x, self.min_y)
            self.pen.down()
            self.pen.setposition(x, self.min_y)
            self.pen.up()
            x += inc # Next x
        inc = (self.max_y - self.min_y) / num
        y = self.min_y
        
        while y <= self.max_y:
            self.pen.setposition(self.min_x, y)
            self.pen.down()
            self.pen.setposition(self.max_x, y)
            self.pen.up()
            y += inc # Next y

    def draw_arrow(self, x1, y1, x2, y2): 
        """ (Plotter, int, int, int, int) -> turtle

        Draws a line segment with an attached arrow head. 
        Expects four numeric parameters representing the (x 1 , y 1 ) tail end 
        point and (x 2 , y 2 ) head end point of the arrow.
        """
        # Draw arrow shaft
        self.pen.up()
        self.pen.setposition(x1, y1) # Move the pen starting point
        self.pen.down()     # Draw line bottom to top
        self.pen.setposition(x2, y2) # Move the pen starting point
        
        # Draw arrow head
        dy = y2 - y1
        dx = x2 - x1

        angle = atan2(dy, dx) * 180 / pi
        self.pen.setheading(angle)
        self.pen.stamp()

    def plot_function(self, f, color, update=True): 
        """ (Plotter, func, str, bool) -> turtle
        Plots the curve of a given function <f> with a specified color,
        established by initialize_plotter.
        Plots (x, f(x)), for all x in range min_x <= x < max_x
        The color parameter dicatates the curve's color

        An optional Boolean parameter determines if the function renders 
        immediately or requires the client to call the update method after a 
        series of plots (defaults to True).    
        """
        # Move pen to starting position
        self.pen.up()
        self.pen.setposition(self.min_x, f(self.min_x))
        self.pen.color(color)
        self.pen.down()

        # Iterate over the range of x values for min_x <= x < max_x
        x = self.min_x
        while x < self.max_x:
            self.pen.setposition(x, f(x))
            x += self.x_increament # Next x

        if update:
            self.screen.update()

    def plot_data(self, data, color, update=True): 
        """ (Plotter, list, str, bool) -> turtle
        
        Plots the curve (x, y) pairs of values in data_list.
        A parameter <color> specifies the curve’s color. 
        An optional Boolean parameter determines if the function renders 
        immediately or requires the client to call the update method after a 
        series of plots (defaults to True).
        """
        self.pen.up()
        self.pen.setposition(data[0][0], data[0][1])
        self.pen.color(color)
        self.pen.down()

        # Plot the points in th data set
        for x, y in data:
            self.pen.setposition(x, y)
        if update:
            self.screen.update()

    def update(self):
        """ (Plotter) -> turtle
        
        Draws any pending actions to the screen 
        """
        self.screen.update()

    def setcolor(self, color): 
        """ (Plotter, str) -> turtle
        
        Sets the current drawing color. 
        """
        self.pen.color(color)
    
    def onclick(self, fun): 
        """ (Plotter, func) -> turtle

        Assigns a callback function that the frame should call when the 
        user clicks the mouse button when the pointer is over the plotter 
        window.
        
        The function <fun> must accept two integer parameters that represent
        the (x, y) location of the mouse when the click occurred
        """
        self.screen.onclick(fun)
    
    def interact(self): 
        """ (Plotter) -> turtle

        Sets the plotter to interactive mode, enabling the user to 
        provide mouse and keyboard input.
        """
        self.screen.mainloop()


