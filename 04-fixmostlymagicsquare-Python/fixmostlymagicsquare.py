# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.
from collections import defaultdict



def get_index(data):
	dict_data = defaultdict(int)
	common_sum = -1
	number = -1
	for ele in data:
		dict_data[ele] += 1
	max_value = max(dict_data.values())
	print(dict_data)
	for key in dict_data:
		if dict_data[key] != max_value:
			number = key
		else:
			common_sum = key
	print("The number: ", number)
	if number == -1:
		return -1
	return [data.index(number), common_sum]


def get_pos(row_sum, col_sum, diag_sum):
	row_index = get_index(row_sum)
	col_index = get_index(col_sum)
	print("The common sum: ", row_index[1])
	if row_index[0] == col_index[0] == -1:
		return (-1,-1,row_index[1])
	else:
		return (row_index[0], col_index[0], row_index[1])
		


def fixmostlymagicsquare(L):
	size = len(L)
	row_sum = [0]*size
	col_sum = [0]*size
	diag_sum = []


	# row sum 
	for i in range(len(L)):
		row_sum[i] = sum(L[i])

	# col_sum
	for j in range(len(L[0])):
		col_sum_value = 0
		for i in range(len(L)):
			col_sum_value += L[i][j]
		col_sum[j] = col_sum_value

	diag_sum_one = 0
	diag_sum_two = 0
	for i in range(len(L)):
		diag_sum_one += L[i][i]

	i = 0
	j = len(L) - 1
	for i in range(len(L)):
		diag_sum_two += L[i][j]
		i += 1
		j -= 1
	diag_sum.append(diag_sum_one)
	diag_sum.append(diag_sum_two)
	postions = get_pos(row_sum, col_sum, diag_sum)
	if postions[0] == postions[1] == -1:
		return L
	print("The found difference:", postions)
	changed_number = postions[2] - L[postions[0]][postions[1]]
	L[postions[0]][postions[1]] = changed_number
	return L

print(fixmostlymagicsquare([[16, 3, 2, 13], [5, 10, 11, 18], [9, 6, 7, 12],[4, 15, 14, 1]]))
	
	



