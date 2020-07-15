# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0


def fun_get_kth_digit(digit, k):
	counter = -1
	result = 0
	while counter < k:
		result = digit % 10
		digit = digit//10
		counter += 1
	# print(result)
	return result


# print(fun_get_kth_digit(789, 3))
print(fun_get_kth_digit(789, 0))
print(fun_get_kth_digit(789, 1))
print(fun_get_kth_digit(789, 2))
print(fun_get_kth_digit(789, 3))
print(fun_get_kth_digit(-789, 0))
print(fun_get_kth_digit(-780, 0))