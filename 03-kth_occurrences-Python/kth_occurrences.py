# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.
from collections import defaultdict

def fun_kth_occurrences(s, n):
	dict_data = defaultdict(int)
	result = ''

	for ele in s:
		dict_data[ele] += 1

	max_count = max(dict_data.values())
	print(max_count)
	print(dict_data)
	counter = 0
	for key in dict_data:
		if dict_data[key] == max:
			counter += 1
			if counter == n:
				return key
	return ''
	
	

print(fun_kth_occurrences("asuszenphonemaxm1 aemnsh",6))


