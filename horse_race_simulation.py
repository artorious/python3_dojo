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
# TODO: Include specif shapes and images for the simulation
import turtle

def new_horse():
    """(None) -> turtle
    Create a new horse
    Returns a turtle object
    """
    horse = turtle.Turtle()
    return horse

def generate_horses(num_horses):
    """(int) -> list
    Returns a list of turtle objects assigned to variable horses
    """
    horses = []
    for a_horse in range(0, num_horses):
        horse = new_horse()
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
    num_horses = 10 # Init number of horses
    turtle.setup(750, 800)  # Set window size
    window = turtle.Screen() # Init turtle window
    window.title('Horse Race Simulation Program') # Set window title bar
    start_loc = (240, -200) # Init Location of the first horse
    track_separation = 60   # Init amount of separation between each horse
    horses = generate_horses(num_horses) # Generate & Init horses
    place_horses(horses, start_loc, track_separation)   # Place horses at starting line
    turtle.exitonclick() # Terminate program when close window


if __name__ == '__main__':
    main()
