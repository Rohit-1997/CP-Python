# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def helper(result, power, n):
	current = 3**power
	if current > n:
		return
	result.append(current)
	helper(result, power+1, n)

def recursion_powersof3ton(n):
	if n < 1:
		return []
	result = []
	helper(result, 0, n)
	return result


print(recursion_powersof3ton(10.5))
