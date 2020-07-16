# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	size = len(a)
	a.sort()
	current_diff = a[1] - a[0]

	for i in range(2,size):
		diff = a[i] - a[i-1]
		if diff < current_diff:
			current_diff = diff

	return current_diff

print(smallestdifference([1, -3, 71, 68, 17]))



