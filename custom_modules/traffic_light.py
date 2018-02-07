#!/usr/bin/env python3
""" Traffic Light  -  class definitions for a traffic light objects.

Illustrates the concept of composition using higher-level objects

An app that graphically models an intersection containing traffic lights. 
Normal traffic light operating procedure changes from; 
    - red to green, 
    - green to yellow, 
    - and yellow to red. 
Other transitions, such as green to red or red to yellow should not be supported. 
"""

import tkinter as tk 
import tkinter.ttk as ttk

class TrafficLamp(object):
    """ Serves as one lamp within a traffic light object """

    def __init__(self, parent, width, order, color='red', *args, **kwargs):
        """Creates a new lamp to be used in a traffic light object.

        parent: The traffic light owning this lamp
        width: The width of the case of the circular lamp
        order: Distance of this lamp from the top of the traffic light
        color: The lamp's initial color (deaults to red)
        *args: Additional args to pass to the ttk.Frame superclass constructor
        **kwargs: Additional keyword arguments to pass to the ttk.Frame 
        suprclass constructor
        """
        
        pass
    
    def turn_on(self):
        """ Illuminates the lamp """
        pass

    def turn_off(self):
        """ Turns off the lamp """
        pass
    
    def resize(self, width):
        """ Resize to <width> """
        pass
    

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
        pass

    def change(self):
        """ Changes traffic light's color to next color in the sequence """

        pass

    def resize(self, width):
        """ Changes traffic light's frame width according to the parameter 
        passed by the caller
        """
        pass

        