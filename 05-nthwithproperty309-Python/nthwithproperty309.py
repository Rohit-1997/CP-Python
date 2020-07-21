# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def is_valid(number):
	digits_data = [False] * 10

	while number > 0:
		digit = number % 10
		digits_data[digit] = True
		number = number // 10
	print(digits_data)
	return False in digits_data


def nthwithproperty309(n):
	if n == 0:
		return 309
	counter = 0
	current_number = 310

	while counter < n:
		number = current_number ** 5
		if is_valid(number):
			counter += 1
		current_number += 1
	return current_number - 1

print(nthwithproperty309(1))

