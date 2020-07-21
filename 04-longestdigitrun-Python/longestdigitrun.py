# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
from collections import defaultdict
def longestdigitrun(n):
	n = str(abs(n))
	current_count = 0
	result = defaultdict(int)
	max_count = 0
	print(n)
	for i in range(len(n) - 1):
		print("The elements under process: ", n[i], n[i + 1])
		if n[i] == n[i + 1]:
			current_count += 1
			result[n[i]] += 1
			if current_count >= max_count:
				max_count = current_count
			print("The result after update: ", result)
		else:
			current_count = 0

	if len(result.keys()) == 0:
		return int(min(list(str(n))))

	final_result = []

	for key in result:
		if result[key] == max_count:
			final_result.append(key)
	return int(min(final_result))

print(longestdigitrun(123330001))


	