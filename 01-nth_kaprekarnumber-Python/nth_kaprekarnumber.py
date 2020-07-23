# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


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



def fun_nth_kaprekarnumber(n):
    if n == 0:
        return 1

    counter = 0
    current_number = 2

    while counter < n:
        if is_valid(current_number):
            counter += 1
            print("The current k number: ", current_number)
        current_number += 1
    return current_number-1

print(fun_nth_kaprekarnumber(10))
# print(is_valid(1000))
    