#!/usr/bin/env python3
""" A graphical interactive program that models traffic lights

Normal traffic light operating procedure changes from; 
    - red to green, 
    - green to yellow, 
    - and yellow to red. 
"""
import tkinter as tk
import tkinter.ttk as ttk

from custom_modules.traffic_light import TrafficLight

class TrafficLightApp(object):
    """ Graphical window that displays a traffic light and change button. """
    
    def __init__(self):
        """ Init """

        root = tk.Tk()  # Create the main window
        root.title('Traffic Light') # Set title bar text
        # Create widget container
        frame = ttk.Frame(root)
        frame.pack()
        # Create a graphical button and ensure it calls the do_button_press 
        # method when the user presses it
        button = ttk.Button(frame, text='Change', command=self.do_button_press)
        # Make traffic light object instance variable
        self.light = TrafficLight(frame, 100, padding=25) # take advantage of the **kwargs parameter to add a padding of 25 pixels around the border of the light.
        # position button and canvas objects
        button.grid(row=0, column=0)
        self.light.frame.grid(row=0, column=1)
        # Start the GUI eventloop
        root.mainloop()
    
    def do_button_press(self):
        """
        The window manger calls this function when the user
        presses the graphical button
        """
        self.light.change()


if __name__ == '__main__':
    # Create and execute a traffic light window
    TrafficLightApp()