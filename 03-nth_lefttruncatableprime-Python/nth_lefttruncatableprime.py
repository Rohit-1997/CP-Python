# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and 
# nthLeftTruncatablePrime(10) returns 53.
import math
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

def check_zeros(number):
    if number == 0:
        return True
    while number > 0:
        digit = number%10
        if digit == 0:
            return True
        number = number // 10
    return False

def is_valid(number):
    digit_count = len(str(number))
    if digit_count == 1:
        return is_prime(number)
    factor = 10**digit_count

    while factor > 1:
        current_number = number % factor
        if not is_prime(current_number):
            return False
        digit_count -= 1
        factor = 10**digit_count
    return True


def fun_nth_lefttruncatableprime(n):
    if n == 0:
        return 2
    current_number = 3
    counter = 0

    while counter < n:
        if check_zeros(current_number):
            current_number += 2
            continue
        if is_valid(current_number):
            print("The valid numbers: ", current_number)
            counter += 1
        current_number += 2

    return current_number - 2

print(fun_nth_lefttruncatableprime(5))
# print(is_valid(3))
