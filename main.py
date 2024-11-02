import turtle as t
import numpy as np

"""
If we iterate on a n-D array it will go through n-1th dimension one by one.

To return the actual values, the scalars, we have to iterate the arrays in each dimension

The function constellation takes an array as an argument. Function works well when taking 2d array. 
for loop - the variable points references an index in stars. Since stars needs to be a 2d array, when going through 
    the iteration points will point to a list made up of 2 values which will be our x and y coordinates. In reference to 
    line 20
while loop - this while loop creates a circle which will be our constellation stars

"""

def constellation (stars):
    for points in stars:
        t.pu()
        count = 0
        t.goto(points[0], points[1])
        while count < 40:
            t.pd()
            t.fd(1)
            t.rt(10)
            count += 1

"""
The array is divided in a grid
Quadrants 1 = top right
Quadrants 2 = bottom right
Quadrants 3 = bottom left
Quadrants 4 = top left
"""
star_point = np.array(
    [   
        [0,0],[30, 45], [58,25], [110, 60], [155,100], # Quadrant 1
        [150,-25], [170,-35], [135,-45], [145, -65], # Quadrant 2
        [-150, -35], [-145, -55], [-120, -150], [-20, -140], [-25, -175], [-30, -185], # Quadrant 3
        [-160, 40], [-95, 80], [-15, 15], [-45, 120], [-70, 150]  # Quadrant 4

    ])

constellation(star_point)
t.done()
