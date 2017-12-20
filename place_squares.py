#!/usr/bin/env python3
"""Draw a square centered at each location the user clicks"""

import turtle

def draw_square(x_pos, y_pos):
    """(int, int) -> turtle
    Draws a 10x10 square centered at each (<x_pos>, <y_pos>)
    """

    turtle.penup()
    turtle.setheading(0) # Ensure the pen is pointed the right direction
    turtle.setposition(x_pos - 5, y_pos - 5) # Center the square
    turtle.pendown()
    for square_face in range(4):
        turtle.forward(10)
        turtle.left(90)
    turtle.update()

# Turn off animation
turtle.tracer(0)
turtle.hideturtle()

# Allow user to place 10x10 squares using the mouse
turtle.onscreenclick(draw_square)

# Start graphics loop
turtle.mainloop()
