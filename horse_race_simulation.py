#!/usr/bin/env python3
""" Horse Race Simulation Program 
Creates a visualisation of a 10 horse race in which horses are moved ahead at
random distance at fixed intervals until there is a winner
"""

import turtle
import random
import time 

# TODO: Control blink rate of the winning horse (PSL time)

def start_horses(horses, banners, finish_line, forward_incr):
    """ (list, list, int, int) -> turtle
    Takes <horses> being a list of horse turtle objects, 
    <banners> being a list of registered (banner) turtle objects, the 
    location of the <finish_line> as an x coordinate value on the turtle 
    screen, and the fundamental increament amount <forward_incr> 
    (each horse is advanced by one to three times this amount)
    """
    # Init    
    have_winner = False 
    early_leading_horse_displayed = False
    midrace_leading_horse_displayed = False
    display_banner(banners[0][0], (70, -300)) # Display "They're Off" banner
    horse_pos = 0 # index into list of horse turtle objects
    # Move horses increamentally until winner is found
    # Check for leading horse - before and after the halfway mark of the race
    while not have_winner:  
        horse = horses[horse_pos]
        horse.forward(random.randint(1,3) * forward_incr)
        # Display mid-race lead banner
        lead_horse = find_lead_horse(horses)
        if horses[lead_horse].position()[0] < -125 and not midrace_leading_horse_displayed:
            display_banner(banners[2][lead_horse], (40, -300))
            midrace_leading_horse_displayed = True
        # Display early lead banner
        elif horses[lead_horse].position()[0] < 125 and not early_leading_horse_displayed:
            display_banner(banners[1][lead_horse], (10, -300))
            early_leading_horse_displayed = True
        # Check for horse over finish line
        if horse.position()[0] < finish_line:   
            have_winner = True
        else:
            horse_pos = (horse_pos + 1) % len(horses)
    return horse_pos

def display_winner(winning_horse, winner_banner):
    """ (int, str) -> turtle 
    Dispaly <winning_horse> by blinking (Controlled by sleep method in PSL 
    time) and shows <winner_banner> 
    """
    # Display "We Have a Winner"  banner
    display_banner(winner_banner, (20, -300))
    # blink winning horse
    show = False # Control blinking (show/hide turtle) - Toggled True/False on each loop
    blink_counter = 10 # Countdown-var (winner blinks 10 times)
    while blink_counter != 0:
        if show:
            winning_horse.showturtle()
            show = False
        else:
            winning_horse.hideturtle()
            show = True
        blink_counter -= 1
        time.sleep(.4)  # Blinking Effect - Slow down switch btw visible & invisible horse    

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

def get_banner_images(num_horses):
    """ (int) -> list
    Returns a list of GIF image files. 
    Each image contains a banner message, each with a unique number 1 - 10
    """
    all_images = []  # Init
    # Get "They're Off" banner image
    images = ['images/theyre_off_banner.gif']   
    all_images.append(images)
    # Get early lead banner images
    images = []
    for a_horse in range(0, num_horses):
        images = images + ['images/lead_at_start_{0}.gif'.format(a_horse + 1)]
    all_images.append(images)
    # Get mid-way lead banner images
    images = []
    for a_horse in range(0, num_horses):
        images = images + ['images/looking_good_{0}.gif'.format(a_horse + 1)]
    all_images.append(images)
    # Get "We have a Winner" banner image
    images = ['images/winner_banner.gif']
    all_images.append(images)
    return all_images

def register_horse_images(images):
    """ (list) -> turtle
    Registers each object(turtle graphic) in <images> list
    """
    for a_horse in range(0, len(images)):
        turtle.register_shape(images[a_horse])

def register_banner_images(images):
    """ (list) -> turtle
    Registers each object(turtle graphic) in <images> list
    """
    for a_horse in range(0, len(images)):
        for a_banner in range(0, len(images[a_horse])):
            turtle.register_shape(images[a_horse][a_banner])

def new_horse(image_file):
    """(str) -> turtle
    Create a new horse where <image_file> is a valid shapename
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
        horses[a_horse].pendown()

def find_lead_horse(horses):
    """ (list) -> int
    Checks position of the <horses> in the list
    Returns the lead horse
    """
    lead_horse = 0 # Init
    for a_horse in range(1, len(horses)):
        if horses[a_horse].position()[0] < horses[lead_horse].position()[0]:
            lead_horse = a_horse
    return lead_horse

def display_banner(banner, position):
    """ (str, tuple) -> turtle
    Displays <banner> (a valid shapename) at
    <position>
    """
    the_turtle = turtle.getturtle()
    turtle.setposition(position[0], position[1])
    turtle.shape(banner)
    turtle.stamp()

def main():
    """ Horse Race Simulation """
    num_horses = 10                             # Init number of horses
    turtle.setup(750, 800)                      # Set window size
    window = turtle.Screen()                    # Init turtle window
    window.title('Horse Race Simulation Program') # Set window title bar 
    turtle.hideturtle()                         # Hide default turtle
    turtle.penup()                              # Prevent drawing from (0,0) to banner position
    start_loc = (240, -200)                     # Init Location of the first horse
    finish_line = -240                          # Init Finish line
    track_separation = 60                       # Init amount of separation between each horse
    forward_incr = 6                            # Init Increament amount
    horse_images = get_horse_images(num_horses) # Init horse images
    banner_images = get_banner_images(num_horses) # Init banner images
    register_horse_images(horse_images)         # Register images
    register_banner_images(banner_images)       # Register images
    horses = generate_horses(horse_images, num_horses)  # Generate & Init horses
    place_horses(horses, start_loc, track_separation)   # Place horses at starting line
    winner = start_horses(horses, banner_images, finish_line, forward_incr) # Start horses
    display_winner(horses[winner], banner_images[3][0]) # Light up to Display winning horse
    turtle.exitonclick()                        # Terminate program when close window


if __name__ == '__main__':
    main()
