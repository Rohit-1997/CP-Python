# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2

def is_prime(number):
	if number <= 1:
		return False
	for i in range(2,number):
		if number % i == 0:
			return False
	return True


def is_palindrome(number):
	return str(number) == str(number)[::-1]


def fun_nth_palindromic_prime(n):
	if n == 0:
		return 2
	counter = 0
	number = 3
	result = -1

	while counter != number:
		print(number)
		if is_prime(number) and is_palindrome(number):
			result = number
			counter += 1
		number += 1
	return number

print(is_palindrome(3))
print(is_prime(3))
# print(fun_nth_palindromic_prime(1))
	