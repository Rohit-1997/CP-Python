# Write the function alternatingSum(a) that takes a list of numbers and returns the 
# alternating sum (where the sign alternates from positive to negative or vice versa). 
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). If the list is empty, return 0.

def fun_alternatingsum(a): 
	if len(a) == 0:
		return 0
	sub_flag = True
	add_flag = False
	sum = 0
	
	for ele in a:
		if sub_flag and not add_flag:
			sum -= ele
			sub_flag = False
			add_flag = True
		elif add_flag and not sub_flag:
			sum += ele
			add_flag = False
			sub_flag = True
	return sum

print(fun_alternatingsum([5,3,8,4]))


