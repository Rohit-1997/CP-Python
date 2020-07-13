# islegaltriangle(s1, s2, s3)
# Write the function islegaltriangle(s1, s2, s3) that takes three int or float values representing
# the lengths of the sides of a triangle, and returns True if such a triangle exists and False
# otherwise. Note from the triangle inequality that the sum of each two sides must be greater
# than the third side, and further note that all sides of a legal triangle must be positive. Hint:
# how can you determine the longest side, and how might that help?

def islegaltriangle(s1, s2, s3):
	sides = [s1, s2, s3]
	longest_side = sides.pop(sides.index(max(sides)))
	print("The longest side: ", longest_side)
	if sum(sides) > longest_side:
		return True
	return False


print(islegaltriangle(1,2,3))
print(islegaltriangle(7,10,5))
print(islegaltriangle(1,10,12))
print(islegaltriangle(1.1,2.1,3.2))
print(islegaltriangle(7.9, 10.1, 5.9))
print(islegaltriangle(1.00012, 10.0009090, 12.0000001))
