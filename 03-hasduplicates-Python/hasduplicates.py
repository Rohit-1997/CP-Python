# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	if L == []:
		return False
	aux_list = []

	for list_data in L:
		for number in list_data:
			if number in aux_list:
				return True
			aux_list.append(number)
	return False

print(hasduplicates([[2, 7, 9], [9, 5, 1], [4, 3, 8]]))