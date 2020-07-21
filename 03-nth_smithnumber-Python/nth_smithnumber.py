# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False
    return True


def is_smith(num, factors):
    factors_sum = 0
    number_sum = 0
    for number in factors:
        while number > 0:
            factors_sum += (number%10)
            number = number // 10

    while num > 0:
        number_sum += (num%10)
        num = num // 10

    return number_sum == factors_sum


def get_prime_factors(number):
    result = []
    for i in range(2, number):
        if number % i == 0:
            if is_prime(i):
                result.append(i)
    return result


def fun_nth_smithnumber(n):
    if n == 0:
        return 4

    smith_list = [4]
    current_number = 5
    counter = 0

    while counter < n - 1:
        print("The current number: ", current_number)
        factors = get_prime_factors(current_number)
        if is_smith(current_number, factors):
            print("The smith number: ", current_number)
            counter += 1
        current_number += 1
    return current_number - 1


# print("The result: ", fun_nth_smithnumber(3))
print(get_prime_factors(27))