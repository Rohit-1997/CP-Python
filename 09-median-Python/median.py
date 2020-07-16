# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	if a == []:
		return None
	a.sort()
	size = len(a)

	if size%2 != 0:
		return a[size//2]
	mid = (size- 1)//2
	print(mid)
	return (a[mid - 1] + a[mid + 1]) / 2

print(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(median([1, 2, 3, 4, 5.5, 5.1, 7, 8, 9, 10]))
# print(median([1]))
# print(median([]))