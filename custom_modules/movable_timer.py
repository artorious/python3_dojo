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
        print('Initializing MovableTimer')
        self.screen.listen()                        # Receive keypress events
        self.screen.onkey(self.start_timer, 's')    # Key to start the timer
        self.screen.onkey(self.stop_timer, 't')     # Key to stop the timer
        self.screen.onkey(self.reset_timer, 'r')    # Key to reset the timer     
        self.screen.ontimer(self.update, 500)       # Set timer event
    
    def draw(self):
        """
        Renders the digital stopwatch within the window
        """
        self.turtle.clear()     # clear screen
        self.turtle.penup()     # Move pen
        self.turtle.setpos(self.x_pos, self.y_pos)
        self.turtle.pendown()
        self.turtle.write(self.digital_time(), font=('Arial', 48, 'normal'))

    def start_timer(self):
        """
        Starts the timer.
        """
        self.start()
    
    def stop_timer(self):
        """
        Stops the timer.
        """
        self.stop()
    
    def reset_timer(self):
        """
        Resets the timer to 00:00:00.
        """
        self.reset()
    
    def update(self):
        """
        Updates the program's view  of the global stopwatch object.
        Called every one-half second
        """
        self.draw()     # Draw the digital display
        # call the update function again after one half second
        self.screen.ontimer(self.update, 500) 

def main():
    # test
    clock = MovableTimer(screen=Screen(), turtle=Turtle(), x_pos=10, y_pos=20)
    clock.run()

if __name__ == '__main__':
    main()
