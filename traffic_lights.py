#!/usr/bin/env python3
""" A graphical interactive program that models traffic lights

Normal traffic light operating procedure changes from; 
    - red to green, 
    - green to yellow, 
    - and yellow to red. 
"""
from tkinter import Tk, Canvas
from tkinter.ttk import Button, Frame
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
        root.title('Traffic Lights')    # Set title bar text
        
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
        """(TrafficLightWindow) -> 

        The window manager calls this function when the user presses
        the graphical button.
        Method simply delegates its work to the change method of its TrafficLight
        instance variable.
        """
        self.light.change()


if __name__ == '__main__':
    # Create and execute a traffic light window
    TrafficLightWindow()
