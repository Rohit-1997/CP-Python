# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def is_valid(number):
	number_length = len(str(number))
	factor = 10**number_length
	return (number**2)%factor == number
		

def nthautomorphicnumbers(n):
	if n == 1:
		return 0
	current_number = 5
	counter = 0

	while counter < n:
		if is_valid(current_number):
			counter += 1
		current_number += 1
	return current_number - 1

		
print(nthautomorphicnumbers(3))