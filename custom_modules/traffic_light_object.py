#!/usr/bin/env python3
""" Traffic Light Objects -  class definition for traffic light objects.

An app that graphically models an intersection containing traffic lights. 
Normal traffic light operating procedure changes from; 
    - red to green, 
    - green to yellow, 
    - and yellow to red. 
Other transitions, such as green to red or red to yellow should not be supported. 

The single program must be able to; 
    - use multiple traffic lights 
    - each light maintains its own independent operation.

Create a TrafficLight class that enables creation of TrafficLight objects. 
Each TrafficLight object should contain instance variables that represents
the light’s position and current color. 
The class constructor could set the light’s position and initial color. 
A change method could transition the light’s current color to its new color, 
ensuring no out-of-sequence color changes.

Users should be able to specify the position and size of traffic light 
objects within the graphics window. 

Users also should be able to specify the light’s initial color. 

After creating a traffic light object, a user can cycle through its color 
states via a change method.
"""

from tkinter import Canvas

class TrafficLight(object):
    """ Models a traffic light """
    
    def __init__(self, x_pos, y_pos, width, canvas, initial_color='red'):
        """ (TraficLight, int, int, int, TK canvas, str) -> canvas, str, 
        canvas, canvas, canvas
        
        Makes a new traffic light object. The light's left-top corner is 
        anchored at the point (<x_pos>, <y_pos>) and is <width> pixels wide.
        Calculates the light’s height and the size and placement of its three 
        lamps from these three parameters. 

        <canvas> a Tk canvas reference from the client makes user responsible
        for setting up the Tk graphics environment before creating a 
        TrafficLight object. The light will render on the <canvas> drawing 
        surface.

        The light's initial color is <initial_color> from the client.

        Throws a ValueError exception if the client attempts to pass an object
        as the last argument that is not a valid string, defaults to "red".

        establishes five instance variables: 
            canvas, color, red_lamp, yellow_lamp, and green_lamp. 
            
        The following indicates their purpose:
            – canvas: 
                After object construction methods must have acces to the 
                canvas object in order to recolor the lamps as necessary. 
                This means each TrafficLight object must store the caller’s
                canvas object.
            – color: 
                This instance variable keeps track of the light’s current color.
            – red_lamp, yellow_lamp, and green_lamp: 
                These instance variables allow methods to access the circle 
                shapes the constructor created via calls to create_oval. 
                The change method needs access to these shapes to be able 
                change the lamps’ colors.
        The change method in the TrafficLight class updates the color instance
        variable to the next color in the light’s sequence of signals and 
        modifies the fill colors of the two lamps affected by the change.

        """
        # Check to see if the supplied color is valid
        if initial_color not in ('red', 'yellow', 'green'):
            raise ValueError('{0} is not a valid color'.format(initial_color))
        
        # Init instance vars
        self.canvas = canvas
        self.color = initial_color

        # Set the individual lamps initial fill fill colors
        red_fill = 'red' if initial_color == 'red' else 'black'
        yellow_fill = 'yellow' if initial_color == 'yellow' else 'black'
        green_fill = 'green' if initial_color == 'green' else 'black'

        # 1/5 of the width will be the basic unit for computing the height of
        # the traffic light and positioning the individual lamps
        unit = width // 5 # Ensure integer division

        # Traffic light frame
        canvas.create_rectangle(
            x_pos, y_pos, x_pos + width, y_pos + 13 * unit, fill='gray'
        )
        
        x_pos = x_pos + unit
        y_pos = y_pos + unit
        diameter = 3 * unit # Diameter (bounding box width) of each lamp

        # Red lamp - currently on
        self.red_lamp = canvas.create_oval(
            x_pos, y_pos, x_pos + diameter, y_pos + diameter, fill=red_fill
        )
        y_pos += 4 * unit

        # Yellow lamp - currently off
        self.yellow_lamp = canvas.create_oval(
            x_pos, y_pos, x_pos + diameter, y_pos + diameter, fill=yellow_fill
        )
        y_pos += 4 * unit

        # Green lamp - currently off
        self.green_lamp = canvas.create_oval(
            x_pos, y_pos, x_pos + diameter, y_pos + diameter, fill=green_fill
        )

    def change(self):
        """ (TrafficLight) -> TK canvas

        Changes the traffic light's color to the next color in the sequence.
        """
        if self.color == 'red':
            self.color = 'green'
            self.canvas.itemconfigure(self.red_lamp, fill='black')  # Turn red off
            self.canvas.itemconfigure(self.green_lamp, fill='green') # Turn green on

        elif self.color == 'green':
            self.color = 'yellow'
            self.canvas.itemconfigure(self.green_lamp, fill='black') # Turn green off
            self.canvas.itemconfigure(self.yellow_lamp, fill='yellow') # Turn yellow on
        
        elif self.color == 'yellow':
            self.color = 'red'
            self.canvas.itemconfigure(self.yellow_lamp, fill='black') # Turn yellow off
            self.canvas.itemconfigure(self.red_lamp, fill='red') # turn ren on

