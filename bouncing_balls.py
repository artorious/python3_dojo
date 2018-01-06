#!/usr/bin/env python3
""" Bouncing Balls Program
Displays one or more bouncing balls within a turtle screen. 
This program utilizes the following programming features:
    + turtle module
    + time module
    + random module
"""

import turtle
import random
import time

def at_left_edge(ball, screen_width):
    """ Handle ball when it hits the left edge of the screen """
    return

def at_right_edge(ball, screen_width):
    """ Handle ball when it hits the right edge of the screen """
    return

def at_top_edge(ball, screen_height):
    """ Handle ball when it hits the top edge of the screen """
    return

def at_botton_edge(ball, screen_height):
    """ Handle ball when it hits the bottom edge of the screen """
    return

def bounce_ball(ball, new_direction):
    """ Handle ball's change in direction when it bounces """
    return

def create_balls(num_balls):
    """ Initialize ball(s) """
    return

def main():
    """ Bouncing Balls
    Simulates bouncing balls in a turtle screen for a specified number
    of seconds
    """
    
    print('Simulates bouncing balls in a turtle screen for a specified number \
        of seconds')    # Program Greeting
    
    screen_width = 800 # Init Screen width
    screen_height = 600 # Init Screen height
    turtle.setup(screen_width, screen_height)   # Set window size
    window = turtle.Screen()    # Create turtle window
    window.title('Bouncing Balls') # Set window title
    # TODO: Input-Error-checking
    num_secs = int(input('Enter number of seconds to run: ')) # Execution time
    num_balls = int(input('Enter number of balls in simulation: ')) # Number of balls
    create_balls(num_balls) # create balls
    start_time = time.time() # Set start time
    
    # Begin Simulation
    terminate = False # Init Loop Condition
    while not terminate: # Enter loop
        pass
    
    turtle.exitonclick() # Exit on Close window
    

if __name__ == '__main__':
    main()
    