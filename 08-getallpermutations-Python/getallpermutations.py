# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then 
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
def helper(current_list, index, size_x,result_list):
	if index == size_x:
		res = tuple(current_list)
		print("The result tuple: ", res)
		result_list.append(res)
	for i in range(index, size_x+1):
		current_list[index], current_list[i] = current_list[i], current_list[index]
		helper(current_list, index+1, size_x,result_list)
		current_list[index], current_list[i] = current_list[i], current_list[index]


def getallpermutations(x):
	# print("The value of x: ", x)
	result_list = []
	size_x = len(x)
	current_list = list(x)
	helper(current_list, 0, size_x-1,result_list)
	# print("The result: ", result_list)
	return result_list

print(getallpermutations('abcd'))