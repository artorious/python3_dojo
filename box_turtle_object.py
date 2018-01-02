#!/usr/bin/env python3
""" Draw a rectangular box in the window """

from turtle import Turtle, mainloop

t = Turtle()    # Create a turtle object

t.pencolor('red')
t.forward(200)
t.left(90)
t.pencolor('blue')
t.forward(150)
t.left(90)
t.pencolor('green')
t.forward(200)
t.left(90)
t.pencolor('black')
t.forward(150)
t.hideturtle()

mainloop()  # Await user input



