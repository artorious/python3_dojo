#!/usr/bin/env python3
""" Graphics with tkinter Objects 
A graphical interactive program that models a traffic light.
On pressing a biutton <change>, The light changes from red to 
green to yellow to red.
"""

from tkinter import Tk, Canvas
from tkinter.ttk import Button, Frame

def do_button_press():
    """
    The window manager will call this function when the user presses the
    graphical button.
    The variables color, canvas, red_lamp, yellow_lamp and green_lamp are 
    global variables that this funtion expects to exist.
    Since we assign only to the color variable, it is the only variable that
    needs explicit global declaration
    """
    global color

    if color == 'red':
        color = 'green'
        canvas.itemconfigure(red_lamp, fill='black') # Turn red off
        canvas.itemconfigure(green_lamp, fill='green') # Turn green on
    
    elif color == 'green':
        color = 'yellow'
        canvas.itemconfigure(red_lamp, fill='black') # Turn green off
        canvas.itemconfigure(green_lamp, fill='yellow') # Turn yellow on

    elif color == 'yellow':
        color = 'red'
        canvas.itemconfigure(red_lamp, fill='black') # Turn yellow off
        canvas.itemconfigure(green_lamp, fill='red') # Turn red on


if __name__ == '__main__':
    # Init global vars
    color = 'red'   # Light's current color
    root = Tk()     # Create main window
    root.title('Traffic Light')

    frame = Frame(root) # Create a frame to hold the widgets
    frame.pack()        # Make the frame fill the entire window

    canvas = Canvas(frame, width=150, height=300) # Create a drawing surface within frame

    # Set up visual aspects of the traffic light
    canvas.create_rectangle(50, 20, 150, 280, fill='gray') # Traffic light frame
    red_lamp = canvas.create_oval(70, 40, 130, 100, fill='red') # Red lamp
    yellow_lamp = canvas.create_oval(70, 120, 130, 180, fill='black') # Yellow lamp
    green_lamp = canvas.create_oval(70, 200, 130, 260, fill='black') # Green lamp

    button = Button(frame, text='Change', command=do_button_press) # Create a graphical button

    # Position button in th containing frame's first row, first column, and 
    # position canvas in the first row, second column (zero origin)
    button.grid(row=0, column=0)
    canvas.grid(row=0, column=1)

    root.mainloop() # Start GUI event loop
    
