# Write the function isFactor(f, n) that takes 
# two int values f and n, and returns True 
# if f is a factor of n, and False otherwise. 
# Note that every integer is a factor of 0.



def fun_isfactor(f, n):
	if f == 0 and n == 0:
		return True
	# every number is a factor of zero
	if f == 0:
		return True
	return n%abs(f) == 0


print(fun_isfactor(2,2))
print(fun_isfactor(2,5))
print(fun_isfactor(2,4))
print(fun_isfactor(0,6))
print(fun_isfactor(6,0))
print(fun_isfactor(0,0))
print(fun_isfactor(-2,4))
