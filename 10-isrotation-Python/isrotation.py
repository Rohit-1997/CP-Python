# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

from collections import defaultdict

def isrotation(x, y):
	dict_data = defaultdict(int)
	x = str(x)
	y = str(y)
	size_x = len(x)
	for i in range(len(x)):
		index = (i+1) % size_x 
		dict_data[x[i]] = x[index]
	print(dict_data)

	for i in range(len(y)):
		if dict_data[y[i]] != y[(i+1)%len(y)]:
			return False
	return True

print(isrotation(10010,10100))

	
