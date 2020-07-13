# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

import math

def find_distance(x1,y1,x2,y2):
	return math.sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)))



def isrighttriangle(x1, y1, x2, y2, x3, y3):
	distance_12 = find_distance(x1, y1, x2, y2)
	distance_13 = find_distance(x1, y1, x3, y3)
	distance_23 = find_distance(x2, y2, x3, y3)

