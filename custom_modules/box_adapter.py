#!/usr/bin/env python3

from graphical_object import GraphicalObject
from box import Box

class BoxAdapter(GraphicalObject):
    """
    A simple, square box graphial object.
    BoxAdapter is a GraphicalObject.
    BoxAdapter has a Box.
    """

    def __init__(self, **kwargs):
        """
        Initializes an adapted box object with a given Turtle screen, pen,
        and (x_pos, y_pos) position
        """        
        self.box = Box(kwargs['screen'], kwargs['turtle'], 
                        kwargs['x_pos'], kwargs['y_pos'], kwargs['width'])
        super(BoxAdapter, self).__init__(**kwargs)
    
    def move_to(self, x_pos, y_pos):
        """
        Repositions the box to (x_pos, y_pos)
        """
        self.box.position(x_pos, y_pos)

    def draw(self):
        """
        Renders the box in the Turtle graphics window
        """
        # self.box.position(self.x_pos, self.y_pos)
        self.box.render()

def main():
    """ Sample client code """
    from turtle import Screen, Turtle

    # Make a Box object via the adapter
    blue_box = BoxAdapter(screen=Screen(), turtle=Turtle(), 
                            x_pos=20, y_pos=20, width=30)
    
    blue_box.run() # Run the graphical program

if __name__ == '__main__':
    main()
        
