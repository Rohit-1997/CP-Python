# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46


def is_tidy(number):
    number = str(number)
    size = len(number)
    if size == 1:
        return True
    for i in range(size - 1):
        if number[i] > number[i+1]:
            return False
    return True


def fun_nth_tidynumber(n):
    if n == 0:
        return 1
    counter = 0
    current_number = 2
    while counter < n:
        if is_tidy(current_number):
            # print("The current tidy number: ", current_number)
            counter += 1
        current_number += 1
    return current_number - 1


print(fun_nth_tidynumber(15))