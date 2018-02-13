#!/usr/bin/env python3
""" A Stop Watch Program 

A stopwatch object that records the number of times the watch has been started 
until it is reset. 
"""
import turtle as t
from custom_modules.counting_stopwatch import CountingStopwatch

timer = CountingStopwatch()

def draw_watch(sw):
    """ Renders the stopwatch object <sw> in a digital hr:min:sec format. """
    # Compute time in hours, minutes and seconds
    seconds = round(sw.elapsed())
    time = ''
    hours =  seconds // 3600    # Compute total hours
    seconds %= 3600             # Update seconds remaining
    minutes = seconds // 60     # Compute minutes
    seconds %= 60               # Update sconds rmaining
    # Each digit occupies two spaces; pad with leading zeros, if neccessary
    time = '{0:0>2}:{1:0>2}:{2:0>2}'.format(hours, minutes, seconds)

    # Draw graphical sting
    t.clear()
    t.penup()
    t.setposition(-200, 0)
    t.pendown()
    t.write(time, font=('Arial', 64, 'normal'))
    t.penup()
    t.setposition(-50, -50)
    t.pendown()
    t.write(sw.counter(), font=('Arial', 24, 'normal'))

def quit():
    """ Quits the program """
    t.bye()

def update():
    """ Updates the program's view of the global stopwatch object """
    draw_watch(timer)       # Draw the digital display
    t.ontimer(update, 500)  # Call the upadte function again after one half-second

t.title('Stopwatch Test')   # Set window's titlebar text
t.onkey(timer.start, 's')   # Call start method of timer if the user presses s
t.onkey(timer.stop, 't')    # Call stop method of timer if user presses t
t.onkey(timer.reset, 'r')   # Call reset method of timer if user presses r
t.onkey(quit, 'q')          # Call quit  function if user presses q
t.listen()                  # Ensure window receives keyboard events
t.delay(0)                  # Draw as fast as possible
t.speed(0)                  # Fastest turtle actions
t.ontimer(update, 500)      # Call update every one half-second
t.hideturtle()              # Do not show the pen when drawing
t.mainloop()                # Start the show