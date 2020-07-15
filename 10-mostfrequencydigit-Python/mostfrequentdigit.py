# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.
from collections import defaultdict

def mostfrequentdigit(n):
	dict_data = defaultdict(int)
	n = abs(n)
	result = []

	while n > 0:
		ele = n % 10
		dict_data[ele] += 1
		n = n // 10
	
	max_value = max(dict_data.values())

	for key in dict_data:
		if dict_data[key] == max_value:
			result.append(key)

	return min(result)
