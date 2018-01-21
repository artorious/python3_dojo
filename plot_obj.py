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
        pass

    def __del__(self): 
        """ (Plotter) -> stdout

        Called when the client no longer uses the plotter object. 

        The interpreter calls this method, also known as destructor, 
        when the object is no longer bound to a reference with in the 
        executing program. 
        Among other times, this happens when the program’s execution 
        terminates.
        """
        pass

    def draw_axes(self, grid=False):
        """ (Plotter, bool) -> turtle

        Draws the x and y axes within the plotting window.

        An option Boolean parameter <grid> controls the drawing of
        accessory horizontal and vertical lines
        """
        pass

    def draw_grid(self, num):
        """ (Plotter, int) -> turtle

        Draws horizontal and vertical accessory reference coordinate 
        lines on the plot. Parameter <num> control the frequency of the 
        reference lines.
        """
        pass
    
    def draw_arrow(self, x1, y1, x2, y2): 
        """ (Plotter, int, int, int, int) -> turtle

        Draws a line segment with an attached arrow head. 
        Expects four numeric parameters representing the (x 1 , y 1 ) tail end 
        point and (x 2 , y 2 ) head end point of the arrow.
        """
        pass

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
        pass

    def plot_data(self, data, color, update=True): 
        """ (Plotter, list, str, bool) -> turtle
        
        Plots the curve (x, y) pairs of values in data_list.
        A parameter <color> specifies the curve’s color. 
        An optional Boolean parameter determines if the function renders 
        immediately or requires the client to call the update method after a 
        series of plots (defaults to True).
        """
        pass

    def update(self):
        """ (Plotter) -> turtle
        
        Draws any pending actions to the screen 
        """
        pass

    def setcolor(self, color): 
        """ (Plotter, str) -> turtle
        
        Sets the current drawing color. 
        """
        pass
    
    def onclick(self, fun): 
        """ (Plotter, func) -> turtle

        Assigns a callback function that the frame should call when the 
        user clicks the mouse button when the pointer is over the plotter 
        window.
        
        The function <fun> must accept two integer parameters that represent
        the (x, y) location of the mouse when the click occurred
        """
        pass
    
    def interact(self): 
        """ (Plotter) -> turtle

        Sets the plotter to interactive mode, enabling the user to 
        provide mouse and keyboard input.
        """
        pass


if __name__ == '__main__':
    Plotter()

    

    

    

