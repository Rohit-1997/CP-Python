# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def isPrime(number):
	if number <= 1:
		return False
	for i in range(2,number):
		if number % i == 0:
			return False
	return True

def fun_hasnoprimes(l):
	for data in l:
		for ele in data:
			if isPrime(ele):
				return False
	return True

