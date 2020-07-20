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
	
	for key in dict_data:
		if dict_data[key] != max_value:
			number = key
		else:
			common_sum = key

	if number == -1:
		return -1
	return [data.index(number), common_sum]


def get_pos(row_sum, col_sum, diag_sum):
	row_index = get_index(row_sum)
	col_index = get_index(col_sum)
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
	for i in range(len(a)):
		row_sum[i] = sum(L[i])

	# col_sum
	for j in range(len(a[0])):
		col_sum_value = 0
		for i in range(len(a)):
			col_sum_value += a[i][j]
		col_sum[j] = col_sum_value

	diag_sum_one = 0
	diag_sum_two = 0
	for i in range(len(a)):
		diag_sum_one += a[i][i]

	i = 0
	j = len(a) - 1
	for i in range(len(a)):
		diag_sum_two += a[i][j]
		i += 1
		j -= 1
	diag_sum.append(diag_sum_one)
	diag_sum.append(diag_sum_two)
	postions = get_pos(row_sum, col_sum, diag_sum)
	if postions[0] == postions[1] == -1:
		return a
	changed_number = postions[2] - a[postions[0]][postions[1]]
	a[postions[0]][postions[1]] = changed_number
	return a


	
	



