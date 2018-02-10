#!/usr/bin/env python3
""" A graphical interactive program that models traffic lights

Normal traffic light operating procedure changes from; 
    - red to green, 
    - green to yellow, 
    - and yellow to red. 
"""
from tkinter import Tk, Canvas
from tkinter.ttk import Button, Frame
from random import choice, randrange
from functools import partial
from custom_modules.traffic_light_object import TrafficLight

class TrafficLightWindow(object):
    """ Graphical window that dispalys a traffic light and change button. """

    def __init__(self):
        """ (TrafficLightWindow) -> TrafficLight

        Initialization function.
        Creates a Canvas object and uses that to create a TrafficLight object. 
        Creates a tkinter.ttk Button object, and wires it into the 
        do_button_press method.
        """
        root = Tk()             # Create the main window
        root.title('Traffic Light')    # Set title bar text
        
        # Create widget container
        frame = Frame(root) # Create a frame to hold the widgets
        frame.pack()        # Make the frame fill the entire window

        # Create a graphical button and ensure it calls the do_button_press
        # method when the user presses it
        button = Button(frame, text='Change', command=self.do_button_press)
        
        # Create and add a drawing surface within the window
        canvas = Canvas(frame, width=200, height=300) 
        
        # Init a traffic light object instance variable
        self.light = TrafficLight(50,20,100, canvas)

        # Position button in th containing frame's first row, first column, and 
        # position canvas in the first row, second column (zero origin)
        button.grid(row=0, column=0)
        canvas.grid(row=0, column=1)

        root.mainloop() # Start GUI event loop

    def do_button_press(self):
        """(TrafficLightWindow) -> TrafficLight

        The window manager calls this function when the user presses
        the graphical button.
        Method simply delegates its work to the change method of its TrafficLight
        instance variable.
        """
        self.light.change()

class MultisizeLightsWindow(object):
    """
    Graphical window that dispalys multiple traffic lights (different sizes) 
    and change buttons.
    """
    def __init__(self):
        """ (MultisizeLightWindow) -> list
        """
        root = Tk()     # Create the main window
        root.title('Multiple Traffic Lights') # Set title bar text
        self.lights = [] # Init list of traffic light objects

        # The outer frame holds the nine inner frames that each contain 
        # a canvas and a button
        outer_frame = Frame(root)
        outer_frame.pack()

        # Create nine drawing surfaces within the window
        # determine the exact location and size of each light it creates
        for i in range(1, 10):
            # Place widget: One traffic light object and one button object
            f = Frame(outer_frame, borderwidth=2, relief='groove')
            # position widget within grid of rows and columns within its parent
            f.grid(row=0, column=i)
            c = Canvas(f, width=20 * i, height=250)
            c.grid(row=0, column=0)
            self.lights.append(TrafficLight(5*i, 10, 10 * i, c))
            # b =  Button(f, text='Change', command=lambda x=i: lights[x - 1].change())
            b = Button(
                f, text='Change', command=partial(self.do_button_press, i - 1)
            ) 
            b.grid(row=1, column=0)
        
        root.mainloop() # Start the GUI event loop           
            
    def do_button_press(self, idx):
        """(TrafficLightWindow) -> TrafficLight

        The window manager calls this function when the user presses
        the graphical button.
        Method simply delegates its work to the change method of its TrafficLight
        instance variable.
        """
        self.lights[idx].change()

class RandomLightsWindow(object):
    """
    Graphical window that displays multiple random traffic lights of 
    different sizes
    """
    def __init__(self):
        """ (MultisizeLightWindow) -> list
        """
        root = Tk()     # Create the main window
        root.title('Multiple Random Traffic Lights') # Set title bar text
        f = Frame(root)
        f.pack()
        canvas = Canvas(f, width=800, height=600) # Create a drawing surface within the window
        color_list = ['red', 'yellow', 'green']
        self.lights_list = [] # Init list of traffic light objects
        
        for i in range(50):
            self.lights_list.append(TrafficLight(
                randrange(2, 700),
                randrange(2, 400),
                randrange(5, 120),
                canvas,
                choice(color_list)
            ))
        # Create a graphical button and ensure it calls the do_button_press
        # function when the user presses it
        button = Button(f, text='Change', command=self.do_button_press)
        # Position button and canvas objects
        button.grid(row=0, column=0)
        canvas.grid(row=0, column=1)

        root.mainloop() # Start the GUI event loop
    
    def do_button_press(self):
        """
        The window manager calls this function when the user
        presses the graphical button
        """
        for light in self.lights_list:
            light.change()

if __name__ == '__main__':
    # Create and execute one, multiple or random traffic lights 
    TrafficLightWindow()
    # RandomLightsWindow()
    # MultisizeLightsWindow()