# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

def is_valid(number):
    number_squared = str(number**2)
    number_length = len(number_squared)
    if number_length == 1:
        return False
    left_half = int(number_squared[:number_length//2])
    right_half = int(number_squared[number_length//2:number_length])
    return (left_half + right_half) == number


def fun_nth_kaprekarnumber(n):
    if n == 0:
        return 1

    counter = 0
    current_number = 2

    while counter < n:
        if is_valid(current_number):
            counter += 1
        current_number += 1
    print("The result: ", current_number)
    return current_number-1

print(fun_nth_kaprekarnumber(1))
    