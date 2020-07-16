# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).
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
		# print(sum)
		if sum == 1:
			return True
		if sum in dict_data:
			return False
		dict_data[sum] = 1
		n = sum	
	return False

def isPrime(n):
	if n <= 1:
		return False
	for i in range(2,n):
		if n%i == 0:
			return False
	return True


def fun_nth_happy_prime(n):
	if n == 0:
		return 7
	counter = 0
	number = 8

	while counter != n:
		result = ishappynumber(number)
		print("The result: ", result, number)
		if isPrime(number):
			print("in counter")
			counter += 1
			print("The counter: ", counter)
		number += 1
	return number - 1

# print(isPrime(13))
print(fun_nth_happy_prime(1))
print(ishappynumber(11))