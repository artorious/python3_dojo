#!/usr/bin/env python3
""" A play on Local Function Definitions """

from math import fabs

def surface_area(x1, y1, z1,  x2, y2, z2,  x3, y3, z3,  x4, y4, z4,
                x5, y5, z5,   x6, y6, z6,  x7, y7, z7,  x8, y8, z8):
    """(floats) -> float
    Computes the surface area of a rectangular box (cuboid) defined by the 
    3D points (x,y,z) of it's eight corners

        7------8
       /|     /|
      3------4 |
      | |    | |
      | 5----|-6
      |/     |/
      1------2

    """

    # Local helper function to compute area
    def area(length, width):
        """ Computes the area of a <length> x <width> rectangle """
        return length * width
    
    # Init dimensions
    length = fabs(x2 - x1)
    height = fabs(y3 - y1)
    width = fabs(z5 - z1)

    front_area = area(length, height) # Front face
    side_area = area(width, height) # Side face
    top_area = area(length, width) # Top face

    # Surface Area: front/back face, left/right face, top/bottom face
    return (2 * front_area) + (2 * side_area) + (2 * top_area) 

def volume(length, width, height):
    """ (float, float, float) -> float
    Computes the volume of a rectangular box (cuboid) defined by it's
    length, width and height
    """
    return length * width * height

def get_point(msg):
    """(str) -> tuple
    prints a message specified by <msg> and allows the user to enter the
    (x, y, z) coordinates of a point. 
    Returns the point as a tuple
    """
    print(msg)
    x = float(input('Enter x coordinate: '))
    y = float(input('Enter y coordinate: '))
    z = float(input('Enter z coordinate: '))

    return x, y, z

def main():
    """
    Get coordinates of the box's corners from the user
    Compute then display surface area and volume of the box
    """

    print('Enter the coordinates of the box\'s corners')
    print(''' 

        7------8
       /|     /|
      3------4 |
      | |    | |
      | 5----|-6
      |/     |/
      1------2
    
    ''')

    x1, y1, z1 = get_point('Corner 1')
    x2, y2, z2 = get_point('Corner 2')
    x3, y3, z3 = get_point('Corner 3')
    x4, y4, z4 = get_point('Corner 4')
    x5, y5, z5 = get_point('Corner 5')
    x6, y6, z6 = get_point('Corner 6')
    x7, y7, z7 = get_point('Corner 7')
    x8, y8, z8 = get_point('Corner 8')

    print('Surface Area: {0}'.format(surface_area(
        x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, x5, y5, z5, 
        x6, y6, z6, x7, y7, z7, x8, y8, z8
    )))

    # Init dimensions
    length = fabs(x2 - x1)
    height = fabs(y3 - y1)
    width = fabs(z5 - z1)

    print('Volume : {0}'.format(volume(length, width, height)))

if __name__ == '__main__':
    main()

