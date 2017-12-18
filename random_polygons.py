#!/usr/bin/env
'''Draw random sized polygons'''

import turtle
import random
from custom_modules.turtle_templates import polygon
from custom_modules.get_positive_number_from_user import get_positive_num

# Disable rendering to speed up drawing
turtle.hideturtle()
turtle.tracer(0)

print('How many random polygons')
how_many = int(get_positive_num()) 

for a_polygon in range(how_many):   # call polygon() 
    polygon(
        random.randrange(3, 11),        # 3-11 sides
        random.randrange(10, 51),       # length ranges
        random.randrange(-250, 251),    # x-axis position ranges
        random.randrange(-250, 251),    # y-axis position ranges
        random.choice(('red', 'lime', 'cyan', 'yellow', 'purple'))  # Select color at random from tuple
    )
turtle.update() # Render image
turtle.exitonclick() # mouse click to exit