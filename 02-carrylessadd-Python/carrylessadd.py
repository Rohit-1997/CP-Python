# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
	result_list = []
	while x > 0 and y > 0:
		x_digit = x % 10
		y_digit = y % 10
		sum_digit = (x_digit + y_digit)%10
		result_list.insert(0,sum_digit)
		x = x // 10
		y = y // 10
	
	print(result_list)

print(fun_carrylessadd(785, 376))

