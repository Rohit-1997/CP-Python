# Pool balls are arranged in balls where the first row contains 1 pool ball and each row contains 1
# more pool ball than the previous row. 
# numberOfPoolBallRows(balls) that takes a non-negative int number of pool balls, and returns the 
# smallest int number of balls required for the given number of pool balls. Thus, numberOfPoolBallRows(6) 
# returns 3. Note that if any balls must be in a row, then you count that row, and so 
# numberOfPoolBallRows(7) returns 4 (since the 4th row must have a single ball in it).

def fun_numberofpoolballrows(balls):
	ball_count = 0
	total_rows = 0
	row_coutner = 1
	done = False
	
	while not done:
		if ball_count == balls:
			done = True
			break
		for i in range(row_coutner):
			if ball_count == balls:
				done = True
			ball_count += 1
		total_rows += 1
		row_coutner += 1

	print("The row count: ", total_rows)
	return total_rows


print(fun_numberofpoolballrows(7))