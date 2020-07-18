# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 

def factorial(number):
	if number == 0:
		return 1
	elif number == 1:
		return 1
	return number * factorial(number - 1)

def fun_pascaltrianglevalue(row, col):
	if col <= row:
		nume = factorial(row)
		deno = factorial(col) * factorial(row - col)
		return nume / deno