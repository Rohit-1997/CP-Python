# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)

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
		print(sum)
		if sum == 1:
			return True
		if sum in dict_data:
			return False
		dict_data[sum] = 1
		n = sum
		
	return False

def fun_nth_happy_number(n):
	if n == 0:
		return 1
	counter = 0
	number = 0

	while counter != n:
		result = ishappynumber(number)
		if result:
			counter += 1
		number += 1
	return number - 1


print(fun_nth_happy_number(1))