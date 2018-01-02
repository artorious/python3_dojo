#!/usr/bin/env python3
""" Draws in the window a spiral surrounded with an octogon """

from turtle import *

def octogon(t_obj, x_pos, y_pos, color):
    """ (turtle, int, int, str) -> turtle
    Draws with turtle <t_obj>, an octogon centered at (x_pos, y_pos)
    with the specifid color
    """
    t_obj.pencolor(color)
    t_obj.penup()
    t_obj.setposition(x_pos, y_pos)
    t_obj.pendown()
    # Draw eight sides
    for i in range(8):
        t_obj.forward(80)
        t_obj.right(45)

def spiral(t_obj, x_pos, y_pos, color):
    """ (turtle, int, int, str) -> turtle
    Draws with turtle <t_obj>, a spiral centered at (x_pos, y_pos)
    with the specifid color
    """
    distance = 0.2
    angle = 40

    t_obj.pencolor(color)
    t_obj.penup()
    t_obj.setposition(x_pos, y_pos)
    t_obj.pendown()
    # draw spiral
    for i in range(100):
        t_obj.forward(distance)
        t_obj.left(angle)
        distance += 0.5

if __name__ == '__main__':
    t = Turtle()
    octogon(t, -45, 100, 'red')
    spiral(t, 0, 0, 'blue')
    t.hideturtle()
    done()