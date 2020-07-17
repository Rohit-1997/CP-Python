# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def isPrime(n):
	if n <= 1:
		return False

	for i in range(2,n):
		if n%i == 0:
			return False
	return True 

def add_digits(number):
	if number == 0:
		return 0
	sum = 0
	while number > 0:
		sum += (n%10)
		number = number // 10
	return sum


def fun_nth_additive_prime(n):
	if n == 0:
		return 2
	counter = 0
	number = 3
	result = -1

	while counter != n:
		added_res = add_digits(number)
		if isPrime(added_res):
			result = added_res
		number += 1
		counter += 1
	return result
		

