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
    """ (int, int) -> bool
    Handle ball when it hits the left edge of the screen 
    """
    if ball.xcor() < -screen_width / 2:
        return True
    else:
        return False

def at_right_edge(ball, screen_width):
    """ (int, int) -> bool
    Handle ball when it hits the right edge of the screen 
    """
    if ball.xcor() > screen_width / 2:
        return True
    else: 
        return False

def at_top_edge(ball, screen_height):
    """ (int, int) -> bool
    Handle ball when it hits the top edge of the screen 
    """
    if ball.ycor() > screen_height / 2:
        return True
    else:
        return False

def at_bottom_edge(ball, screen_height):
    """ (int, int) -> bool
    Handle ball when it hits the bottom edge of the screen 
    """
    if ball.ycor() < -screen_height / 2:
        return True
    else:
        return False

def bounce_ball(ball, new_direction):
    """ (int, str) -> int
    Handle ball's change in direction when it bounces
    Returns the new heading
    """
    if new_direction == 'left' or new_direction == 'right':
        new_heading = 180 - ball.heading()
    elif new_direction == 'up' or new_direction == 'down':
        new_heading = 360 - ball.heading()
    return new_heading

def create_balls(num_balls):
    """ (int) -> list
    Initialize <num_balls>
    Returns a list populated with <num_balls> 
    """
    balls = []
    for each_ball in range(0, num_balls):
        new_ball = turtle.Turtle()
        new_ball.shape('circle')
        new_ball.fillcolor('black')
        new_ball.speed(0)
        new_ball.penup()
        new_ball.setheading(random.randint(1, 359))
        balls.append(new_ball)
    return balls
        
def main():
    """ Bouncing Balls
    Simulates bouncing balls in a turtle screen fo
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
    balls = create_balls(num_balls) # create balls
    start_time = time.time() # Set start time
    
    # Begin Simulation
    terminate = False # Init Loop Condition
    while not terminate: # Enter loop
        for each_ball in range(0, len(balls)):
            balls[each_ball].forward(15)

            if at_left_edge(balls[each_ball], screen_width):
                balls[each_ball].setheading(bounce_ball(balls[each_ball], 'right'))
            elif at_right_edge(balls[each_ball], screen_width):
                balls[each_ball].setheading(bounce_ball(balls[each_ball], 'left'))
            elif at_top_edge(balls[each_ball], screen_height):
                balls[each_ball].setheading(bounce_ball(balls[each_ball], 'down'))
            elif at_bottom_edge(balls[each_ball], screen_height):
                balls[each_ball].setheading(bounce_ball(balls[each_ball], 'up'))
            
            if time.time() - start_time > num_secs:
                terminate = True
    
    turtle.exitonclick() # Exit on Close window
    

if __name__ == '__main__':
    main()
    