#!/usr/bin/env python3
""" Traffic Light  -  class definitions for a traffic light object.

Illustrates the concept of composition using higher-level objects

Utilized by an app that graphically models traffic lights. 
Normal traffic light operating procedure changes from; 
    - red to green, 
    - green to yellow, 
    - and yellow to red. 
Other transitions, such as green to red or red to yellow should not be supported. 
"""

import tkinter as tk # Canvas
import tkinter.ttk as ttk   # Handle graphics

class TrafficLamp(object):
    """ Serves as one lamp within a traffic light object """

    def __init__(self, parent, width, order, color='red', *args, **kwargs):
        """Creates a new lamp to be used in a traffic light object.

        parent: The traffic light owning this lamp
        width: The width of the case of the circular lamp
        order: Distance of this lamp from the top of the traffic light
        color: The lamp's initial color (deaults to red)

        For special control over the style of the frame object,
        
        *args: Additional args to pass to the ttk.Frame superclass constructor
        **kwargs: Additional keyword arguments to pass to the ttk.Frame 
        suprclass constructor
        """
        
        self.frame = ttk.Frame(parent.frame, *args, **kwargs)
        self.canvas = tk.Canvas(
            self.frame, width=width, height=width, bg='gray', 
            highlightthickness=0)
        self.canvas.pack()
        self.color = color
        offset = width // 8
        self.lamp = self.canvas.create_oval(
            offset, offset, 7 * offset, 7 * offset, fill='black')
        # place the lamp in its proper place in the traffic light
        self.frame.grid(row=order, column=0)
        self.state = 'off'
    
    def turn_on(self):
        """ Illuminates the lamp """
        
        self.state = 'on'
        self.canvas.itemconfigure(self.lamp, fill=self.color)

    def turn_off(self):
        """ Turns off the lamp """
        
        self.state = 'off'
        self.canvas.itemconfigure(self.lamp, fill='black')
    
    def resize(self, width):
        """ Resize to <width> """
        
        self.canvas.config(width=width, height=width)
        offset = width // 8
        self.canvas.coords(self.lamp, offset, offset, 7 * offset, 7 * offset)

class TrafficLight(object):
    """ Models a simple traffic light widget """
    
    def __init__(self, root, wd, initial_color='red', *args, **kwargs):
        """ Makes a new traffic light object.

        root: parent widget
        wd: pixels width
        initial_color: Defaults to red
        Clients may pass addtitional arguments to the constructor of the 
        light's frame via *args and **kwargs.
        """
        # check to see if the supplied color is valid
        if initial_color not in ('red', 'yellow', 'green'):
            raise ValueError('{0} is not a valid color'.format(initial_color))

        # Create the widget frame for the light
        self.frame = ttk.Frame(root, width=wd, *args, **kwargs)

        self.frame.grid(row=0, column=0)    # Only widget in a 1x1 grid
        self.color = initial_color # Set initial color
        # Make lamp objects and store them in a dictionary keyed by their color
        self.lamps = dict(zip(('red', 'yellow', 'green'),
                            (TrafficLamp(self, wd, 0, 'red'),
                            TrafficLamp(self, wd, 1, 'yellow'),
                            TrafficLamp(self, wd, 2, 'green'))))
        
        # Turn on lamp for initial color
        self.lamps[self.color].turn_on()

    def change(self):
        """ Changes traffic light's color to next color in the sequence """
        
        # First, determine which color should be next
        if self.color == 'red':
            new_color = 'green'
        
        elif self.color == 'green':
            new_color = 'yellow'
        
        elif self.color == 'yellow':
            new_color = 'red'
        
        # Next, activate and deactivate the appropriate lamps
        self.lamps[self.color].turn_off()
        self.color = new_color
        self.lamps[self.color].turn_on()

    def resize(self, width):
        """ Changes traffic light's frame width according to the parameter 
        passed by the caller
        """
        # Resize each lamp in the dictionary of lamps
        for lamp in self.lamps.values():
            lamp.resize(width)

