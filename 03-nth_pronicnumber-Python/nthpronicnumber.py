# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def nthpronicnumber(n):
	if n == 0:
		return 0
	prev_number = 1
	current_number = 2
	result = 0
	counter = 0

	while counter < n:
		result = prev_number * current_number
		counter += 1
		prev_number = current_number
		current_number += 1
	return result

print(nthpronicnumber(3))
