# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).
import math
def is_prime(number):
	if number <= 1:
		return False
	for i in range(2,int(math.sqrt(number))+1):
		if number % i == 0:
			return False
	return True


def is_valid(number):
	original_number = number
	while is_prime(number):
		number_str = str(number)
		currrent_number_str = number_str[-1] + number_str[0:len(number_str) - 1]
		number = int(currrent_number_str)
		print("The number rotated: ", number, original_number)
		if number == original_number:
			return True
	return False


def nthcircularprime(n):
	if n == 0:
		return 2
	current_number = 3
	counter = 1

	while counter < n:
		if is_valid(current_number):
			counter += 1
		current_number += 2
	return current_number - 2

print(nthcircularprime(5))
