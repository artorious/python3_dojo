#!/usr/bin/env python3
""" Graphics with tkinter Objects 
A simple example that execises a graphical button
"""
from tkinter import Tk, Button

count = 0 # Record/track  no. of button presses

def update():
    """ Update the count label within the graphical button """
    global count, b
    count += 1
    b.config(text='Click Count = {0}'.format(str(count)))
    print('Updating...')


if __name__ == '__main__':
    root = Tk()
    b = Button(root)
    b.configure(background='yellow', text='Click Count = 0', command=update)
    b.pack()
    root.mainloop()