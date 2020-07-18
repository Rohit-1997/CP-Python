# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.
from collections import defaultdict

def fun_kth_occurrences(s, n):
	dict_data = defaultdict(int)
	result = ''

	for ele in s:
		dict_data[ele] += 1

	result_list = sorted(s, key=lambda  x: dict_data[x], reverse=True)
	print(result_list)


print(fun_kth_occurrences("england",1))


