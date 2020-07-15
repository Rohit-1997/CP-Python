# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.

def fun_nearestodd(n):
	res = int(n)
	if res % 2 != 0:
		return res
	res_one = res - 1
	res_two = res + 1
	if (n-res_one) < (res_two - n):
		return res_one
	else:
		return res_two

