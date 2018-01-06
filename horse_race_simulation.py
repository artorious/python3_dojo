#!/usr/bin/env python3
""" Horse Race Simulation Program """
### THE PROBLEM
# Create a visualisation  of a horse race in which horses are moved ahead at
# random distance at fixed intervals until there is a winner
### PROGRAM DESIGN
# Meeting the program requirements
    # Create an appropriate simulation of a 10 horse race
# Data description
    # Current location of each of the 10 horses in a given race
    # Maintain 10 turtle objects (attributes include shape & coordinates)
    # Use/create suitable horse images
# Algorithmic approach
    # Advance each horse at a random distance at fixed intervals until one
    # reaches a certain point on the turtle screen (finish line)
#-----------------------------------------------------------------------------

# TODO: Execute race horse simulation
# TODO: Add Race Banners

import turtle
import random

def start_horses(horses, finish_line, forward_incr):
    """ (list, int, int) -> turtle
    Takes <horses> being a list of horse turtle objects, the location of the
    <finish_line> as an x coordinate value on the turtle screen, and the 
    fundamental increament amount <forward_incr> (each horse is advanced by 
    one to three times this amount)
    """
    # Init    
    have_winner = False 
    horse_pos = 0 # index into list of horse turtle objects
    while not have_winner:  # Move horses increamentally until winner is found
        horse = horses[horse_pos]
        horse.forward(random.randint(1,3) * forward_incr)
        if horse.position()[0] < finish_line:   # Check for horse over finish line
            have_winner = True
        else:
            horse_pos = (horse_pos + 1) % len(horses)
    return horse_pos

def display_winner(winning_horse):
    """ """
    print('Horse {0} Wins!'.format(winning_horse))

def get_horse_images(num_horses):
    """ (int) -> list
    Returns a list of GIF image files. 
    Each image contains the same horse image, each with a unique number 1 - 10
    """
    images = []
    # Get all horse images
    for a_horse in range(0, num_horses):
        images = images + ['images/horse_{0}_image.gif'.format(a_horse + 1)]
    return images

def register_horse_images(images):
    """ (list) -> turtle
    Registers each object(turtle graphic) in <images> list
    """
    for a_horse in range(0, len(images)):
        turtle.register_shape(images[a_horse])

def new_horse(image_file):
    """(file) -> turtle
    Create a new horse
    Returns a turtle object
    """
    horse = turtle.Turtle()
    horse.hideturtle()
    horse.shape(image_file)
    return horse

def generate_horses(images, num_horses):
    """(list, int) -> list
    Returns a list of turtle objects assigned to variable horses
    """
    horses = []
    for a_horse in range(0, num_horses):
        horse = new_horse(images[a_horse])
        horses.append(horse)
    return horses

def place_horses(horses, loc, separation):
    """ (list, tuple, int) -> turtle
    Positions each turtle object in <horses>, 
    <loc> being coordinates for the first turtle, 
    and the amount of <separation> between each
    horse
    """
    for a_horse in range(0, len(horses)):
        horses[a_horse].hideturtle()
        horses[a_horse].penup()
        horses[a_horse].setposition(loc[0], loc[1] + a_horse * separation)
        horses[a_horse].setheading(180)
        horses[a_horse].showturtle()

def main():
    """ Horse Race Simulation """
    num_horses = 10                             # Init number of horses
    turtle.setup(750, 800)                      # Set window size
    window = turtle.Screen()                    # Init turtle window
    window.title('Horse Race Simulation Program') # Set window title bar 
    start_loc = (240, -200)                     # Init Location of the first horse
    finish_line = -240                          # Init Finish line
    track_separation = 60                       # Init amount of separation between each horse
    forward_incr = 6                            # Init Increament amount
    horse_images = get_horse_images(num_horses) # Init horse images
    register_horse_images(horse_images)         # Register images
    horses = generate_horses(horse_images, num_horses)  # Generate & Init horses
    place_horses(horses, start_loc, track_separation)   # Place horses at starting line
    winner = start_horses(horses, finish_line, forward_incr) # Start horses
    display_winner(winner + 1)                  # Display winning horse
    turtle.exitonclick()                        # Terminate program when close window


if __name__ == '__main__':
    main()
