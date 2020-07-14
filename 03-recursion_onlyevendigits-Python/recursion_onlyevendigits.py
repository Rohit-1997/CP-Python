# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def number_breakdown(number,mp):
	print("The number: ", number)
	if number == 0:
		return 0
	units = number % 10
	print("The units: ", units)
	if units % 2 == 0:
		res = (units * mp) + number_breakdown(number//10, mp*10)
		print("The step result: ", res)
		return res
	return number_breakdown(number//10, mp)


def helper(l, index, result):
	if index == len(l):
		return
	even_num = number_breakdown(l[index], 1)
	print("The result after breaking down: ", even_num)
	result.append(even_num)
	helper(l, index+1, result)

	



def fun_recursion_onlyevendigits(l):
	if l == []:
		return []
	result = []
	helper(l,0, result)
	print(result)

# fun_recursion_onlyevendigits([58344])
print(fun_recursion_onlyevendigits([43, 23265, 17, 58344]))