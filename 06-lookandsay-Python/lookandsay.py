# First, you can read about look-and-say numbers here. Then, write the function lookAndSay(a) that takes a list of 
# numbers and returns a list of numbers that results from "reading off" the initial list using the look-and-say 
# method, using tuples for each (count, value) pair. For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]
from collections import defaultdict

def lookandsay(a):
	if a == []:
		return []

	dict_data = defaultdict(int)
	result = []

	for ele in a:
		dict_data[ele] += 1

	for ele in sorted(dict_data.keys()):
		result.append((dict_data[ele], ele))

	return result

print(lookandsay([3,3,8,3,3,3,3]))

	


	
	