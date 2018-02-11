#!/usr/bin/env python3
""" A graphical object on a Turtle graphics Window """

from multiple_inheritance_sample import Top

class GraphicalObject(Top):
    """ 
    A Graphical object that allows the user to reposition it anywhere
    within the widow using the mouse.
    Contains all the code to manage the Turtle graphics environment.
    """
    
    def __init__(self, **kwargs):
        """ Initializes a GraphicalObject object

        Keyword args include:
            screen is the Turtle graphics screen
            turtle is the Turtle graphics pen
            intially appear at location (x, y)
        """
        super(GraphicalObject, self).__init__(**kwargs) # Explicitly invoke superclass constructor
        print('Initializing graphical object')
        self.screen = kwargs['screen']
        self.turtle = kwargs['turtle']
        self.x_pos = kwargs['x_pos']
        self.y_pos = kwargs['y_pos']
        self.screen.delay(0)                    # Fastest drawing speed
        self.turtle.speed(0)                    # Fastest turtle actions
        self.turtle.hideturtle()                # make turtle invisible
        self.screen.onclick(self.do_click)      # Set mouse press handler
        self.move_to(x_pos=kwargs['x_pos'], y_pos=kwargs['y_pos'])

    def run(self):
        """ Run the graphical program """
        self.screen.mainloop()
    
    def draw(self):
        """ Renders the object within the window.

        Derived classes override this method to meet their specific needs
        """
        pass
    
    def do_click(self, x_pos, y_pos):
        """ Called when the user presses the mouse button

        (<x_pos>, <y_pos>) is the new location of the display
        """
        self.move_to(x_pos, y_pos)  # Move to a new location
        self.draw()                 # Redraw at new location
    
    def move_to(self, x_pos, y_pos):
        """ Relocates a movable object to position (<x_pos>, <y_pos>) """

        self.x_pos, self.y_pos = x_pos, y_pos

