# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	n = str(abs(n))
	current_count = 0
	result = []
	max_count = 0
	print(n)
	for i in range(len(n) - 1):
		if n[i] == n[i + 1]:
			current_count += 1
			if current_count > max_count:
				max_count = current_count
				result.append(int(n[i]))
		else:
			current_count = 0
	print("The result: ", result)
	if result == []:
		return int(min(list(str(n))))

	return min(result)

print(longestdigitrun(112233455567))


	