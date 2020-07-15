# ishappynumber(n) [10 pts]
# A happy number is a number defined by the following process: Starting with any positive integer, replace the 
# number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will 
# stay ), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 
# are happy numbers.

# Write the function ishappynumber(n) which takes a possibly-negative integer and returns True if it is happy and 
# False otherwise. Note that all numbers less than 1 are not happy. Here are some test assertions for you:
# assert(ishappynumber(-7) == False)
# assert(ishappynumber(1) == True)
# assert(ishappynumber(2) == False)
# assert(ishappynumber(97) == True)
# assert(ishappynumber(98) == False)
# assert(ishappynumber(404) == True)
# assert(ishappynumber(405) == False)
from collections import defaultdict

def helper(number):
	sum = 0
	while number > 0:
		digit = number % 10
		sum += (digit**2)
		number = number // 10
	return sum


def ishappynumber(n):
	if n == 1:
		return True

	dict_data = defaultdict(int)
	while True:
		sum = helper(n)
		if sum == 1:
			return True
		if sum in dict_data:
			return False
		dict_data[sum] = 1
	
	return False

print(ishappynumber(23))