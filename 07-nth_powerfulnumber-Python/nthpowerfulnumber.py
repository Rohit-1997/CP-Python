# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.
import math

def is_prime(number):
	if number <= 1:
		return 1
	for i in range(2,int(math.sqrt(number)) + 1):
		if number % i == 0:
			return False
	return True


def get_prime_factors(number):
	factors = []

	while number % 2 == 0:
		factors.append(2)
		number = number // 2

	for i in range(3, int(math.sqrt(number)) + 1, 2):
		while number % i == 0:
			factors.append(i)
			number = number // i

	if number > 2:
		factors.append(number)
	return factors


def is_powerful(number):
	factors = set(get_prime_factors(number))
	print('The prime factors for the numbers: ', number, factors)
	for factor in factors:
		if (factor**2)%number != 0:
			return False
	return True



def nthpowerfulnumber(n):
	if n == 0:
		return 1
	counter = 0
	current_number = 2
	while counter < n:
		if is_powerful(current_number):
			counter += 1
		current_number += 1
	return current_number - 1

print(nthpowerfulnumber(10))
