#!/usr/bin/env python3
""" Kitchen Tile Visualisation Program

Allows the user to select;
    + kitchen tile size, 
    + primary and secondary tile color,
    + frequency in which the secondary color is to be placed,
    + grout color
Displays the resulting tile pattern
"""

import turtle

def greeting():
    """ Displays the program greeting on the screen """
    pass

def get_tile_selections(grout_color_options):
    """ (set) -> dict

    Returns a dictionary of the form, 
    
    {'tile_size':dict, 'color1:str', 'color2:str', 'skip':int, 'grout':str}
    
    where the value of tile_size is a dictionary of the form,
        {'tile_length':value, 'tile_width':value}
    color1 and color2 are the selected primary and secondary color code 
    strings in hexadecimal format, skip is an integer indicating the  number
    of primary colors that occur for every secondary color, and grout contains
    the selected grout color
    """
    return

def layout_tiles(window, selections, tile_area, scaling):
    """ (turtle, dict, dict, int) -> turtle

    Displays the tiles in the window starting with the top and working 
    towards the bottom of the window. 
    This function requires that the coordinate (0,0) be set as the top
    corner of the window
    """
    pass

def kitchen_tiles():
    """ Kitchen Tile Visualisation """
    # Init
    tile_area = {'width': 660, 'height': 440}
    grout_color_selections = {'white', 'gray', 'brown', 'black'}
    scaling = 20
    
    greeting()                                                  # Prog Greeting
    selections = get_tile_selections(grout_color_selections)    # get tile selection and layout dtails
    turtle.setup(tile_area['width'], tile_area['height'])       # Set window size
    window = turtle.Screen()                                    # get reference to turtle window
    window.title('Kitchen Tile Visualisation Program')          # Set window title
    window.setworldcoordinates(0, 0, tile_area['width'], tile_area['height']) # Set coordinate system
    window.mode('world')                                    # Set coordinate system
    layout_tiles(window, selections, tile_area, scaling)    # layout tiles in window
    turtle.exitonclick()                                    # terminate program when window closed



if __name__ == '__main__':
    kitchen_tiles()