# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def ismostlymagicsquare(a):
	if a == [] or a == [[]]:
		return False
	row_sum = 0
	col_sum = 0
	diag_sum_one = 0
	diag_sum_two = 0

	# row sum
	for i in range(len(a)):
		if i == 0:
			row_sum = sum(a[i])
		else:
			if sum(a[i]) != row_sum:
				return False
	
	# column sum
	for j in range(len(a[0])):
		current_col_sum = 0
		for i in range(len(a)):
			current_col_sum += a[i][j]
		if j == 0:
			col_sum = current_col_sum
		elif current_col_sum != col_sum:
				return False
	
	print("The row sum, column sum: ", row_sum, col_sum)


	for i in range(len(a)):
		diag_sum_one += a[i][i]
	
	for i in range(len(a)):
		for j in range(len(a[0]) - 1, -1, -1):
			print(a[i][j])
			diag_sum_two += a[i][j]
	print("The diagonal sums: ", diag_sum_one, diag_sum_two)
	if diag_sum_one != diag_sum_two:
		return False
	else:
		return row_sum == col_sum == diag_sum_one


			
print(ismostlymagicsquare([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))



		


		