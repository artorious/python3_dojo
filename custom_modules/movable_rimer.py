#!/usr/bin/env python3

"""
Defines a class named MovableTimer that inherits from both DigitalTimer
and GraphicalObject.
"""
from digital_timer import DigitalTimer
from graphical_object import GraphicalObject
from turtle import Screen, Turtle

# class MovableTimer(DigitalTimer, GraphicalObject):
class MovableTimer(GraphicalObject, DigitalTimer):
    """
    A graphical digital timer that allows the user to reposition it's display
    anywhere within the window using the mouse. 
    Contains all the code to manage th Turtle graphics environment.
    """

    def __init__(self, **kwargs):
        """
        Sets the graphical environment and initial position of the display
        (x_pos, y_pos) is the display's initial position
        """
        super(MovableTimer, self).__init__(**kwargs)
        pass
    
    def draw(self):
        """
        Renders the digital stopwatch within the window
        """
        pass

    def start_timer(self):
        """
        Starts the timer.
        """
        pass
    
    def stop_timer(self):
        """
        Stops the timer.
        """
        pass
    
    def reset_timer(self):
        """
        Resets the timer to 00:00:00.
        """
        pass
    
    def update(self):
        """
        Updates the program's view  of the global stopwatch object.
        Called every one-half second
        """
        pass

def main():
    # test
    clock = MovableTimer(screen=Screen(), turtle=Turtle(), x_pos=10, y_pos=20)
    clock.run()

if __name__ == '__main__':
    main()
