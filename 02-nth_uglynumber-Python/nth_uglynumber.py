# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.
def get_prime_factors(number):
    result = []

    while number % 2 == 0:
        result.append(2)
        number = number//2

    for i in range(3,number,2):
        while number % i == 0:
            result.append(i)
            number = number // i

    if number > 2:
        result.append(number)
    return result


def is_ugly(number):
    result = get_prime_factors(number)
    print("The prime factors: ", result)
    for ele in result:
        if ele > 5:
            return False
    return True


def fun_nth_uglynumber(n):
    if n == 0:
        return 1
    current_number = 2
    counter = 0

    while counter < n:
        if is_ugly(current_number):
            print("The current ugly number: ", current_number)
            counter += 1
        current_number += 1
    print("The nth ugly number: ", current_number - 1)
    return 0

print(fun_nth_uglynumber(100))
# print(is_ugly(15))
