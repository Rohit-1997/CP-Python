# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# def reverse()

def is_valid(number):
	for i in range(25):
		reverse_number = int(str(number)[::-1])
		number += number
		if (str(number)) == str(number)[::-1]:
			return False
	return True


def nthlychrelnumbers(n):
	if n == 1:
		return 196
	counter = 1
	current_number = 197

	while counter < n:
		if is_valid(current_number):
			print('The current number: ', current_number)
			counter += 1
		current_number += 1
	return current_number - 1


print(nthlychrelnumbers(2))
# print(is_valid(3675))