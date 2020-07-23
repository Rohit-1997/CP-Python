# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.

import math
def is_valid(number):
    number_squared = number**2
    digit_count = len(str(number_squared))
    right_part_count = 0

    while right_part_count < digit_count:
        right_part_count += 1
        split_factor = 10**right_part_count
        # print("The split factor: ", split_factor)
        if split_factor == number:
            continue
        left_part = number_squared//split_factor
        right_part = number_squared%split_factor
        if left_part + right_part == number:
            return True
    return False

def fun_nearestkaprekarnumber(n):
    left_number = n
    right_number = n

    # getting the left number
    while left_number > 0:
        if is_valid(left_number):
            break
        left_number -= 1

    print("The left number: ", left_number)

    while True:
        if is_valid(right_number):
            break
        right_number += 1

    print("The right number: ", right_number)
    if abs(n - left_number) <= abs(right_number - n):
        result = left_number
    else:
        result = right_number
    print("The result is: ", result)
    return result

print(fun_nearestkaprekarnumber(51))
