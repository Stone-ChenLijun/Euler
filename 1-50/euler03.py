from math import sqrt

def prime(max):
    yield 2
    primes = [2]
    num = 3
    while num <= max:
        isPrime = True
        for prime in [x for x in primes if x <= sqrt(num)]:
            if num % prime == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(num)
            yield num
        num += 2

num = 600851475143
temp = num
for prime in prime(sqrt(num)):
    while temp % prime == 0:
        temp /= prime
    if temp == 1:
        print(prime)
        break