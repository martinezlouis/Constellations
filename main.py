import turtle as t
import numpy as np

"""

def  constellation (stars):
    for points in stars:
        for coordinate in points:
            t.fd(coordinate)



t.fd(100)
t.done()
"""

"""
If we iterate on a n-D array it will go through n-1th dimension one by one.

To return the actual values, the scalars, we have to iterate the arrays in each dimension

points will give the index of star_point while coordinate will return the value

"""


star_point = np.array([[124, 222], [116, 200]])
for points in star_point:
    for coordinate in points:
        print(coordinate)







