# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!
import math

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


def sumOfSquaresOfDigits(number):
    if number == 0:
        return 0
    sum = 0
    while number > 0:
        digit = number%10
        sum += digit**2
        number = number // 10
    return sum


def isHappyNumber(number):
    result = number
    while result != 1 and result != 4:
        print("The result before: ", result)
        result = sumOfSquaresOfDigits(result)
        print("The result after: ", result)
    return result == 1



def ishappyprimenumber(n):
    # Your code goes here
    if not is_prime(n):
        return False
    else:
        return isHappyNumber(n)

print(ishappyprimenumber(833))