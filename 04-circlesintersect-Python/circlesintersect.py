# Write the function circlesIntersect(x1, y1, r1, x2, y2, r2) 
# that takes 6 numbers (ints) -- x1, y1, r1, x2, y2, r2 -- 
# that describe the circle centered at (x1,y1) with radius r1, 
# and the circle centered at (x2,y2) with radius r2, and returns True 
# if the two circles intersect and False otherwise.

import math

def fun_circlesintersect(x1, y1, r1, x2, y2, r2):
	res = ((x1-x2) * (x1-x2)) + ((y1-y2) * (y1-y2))
	distance = int(math.sqrt(res))
	print(distance)
	total_radius = r1 + r2
	if total_radius == distance or total_radius > distance:
		return True
	return False 


if __name__ == "__main__":
	print(fun_circlesintersect(5, 6, 14, 8, 7, 9))
	print(fun_circlesintersect(-10, 8, 30, 14, -24, 10))
	print(fun_circlesintersect(3, 4, 5, 14, 18, 8))
	print(fun_circlesintersect(2, 3, 12, 15, 28, 10))
