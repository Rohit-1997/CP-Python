# Write the function nthCarolPrime(n), which takes a non-negative int and returns the nth Carol Prime, 
# which is a prime number of the form ((2**k - 1)**2 - 2) for some value positive int k. For example, 
# if k equals 3, ((2**3 - 1)**2 -2) equals 47, which is prime, and so 47 is a Carol Prime. 
# The first several Carol primes are: 7, 47, 223, 959, 3967, 16127, 65023, 261119, 1046527,... As such, 
# nthCarolPrime(0) returns 7.
# Note: You must use a reasonably efficient approach that quickly works up to n==9, which 
# will return a 12-digit answer! In particular, this means you cannot just edit isPrime. 
# Hint: you may need to generate only Carol numbers, and then test those as you go 
# for primality (and you may need to think about that hint for a while for it to make sense!).

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False
    return True


def is_valid(k):
    result = (((2**k) - 1)**2 - 2)
    return is_prime(result), result


def fun_nth_carolprime(n):
    if n == 0:
        return 7
    k = 3
    counter = 0
    while counter < n:
        valid, value = is_valid(k)
        if valid:
            print("The valid value and counter: ", value, counter)
            counter += 1
        k += 1
    return value

print(fun_nth_carolprime(0))
        
    
    