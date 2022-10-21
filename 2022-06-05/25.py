def isPrime(n):
    d = 2
    while d ** 2 <= n:
        if n % d == 0:
            return False
        d += 1
    return True

primes = []
for i in range(3, 10**6):
    if isPrime(i):
        primes.append(i)

for i in range(len(primes) - 1):
    if primes[i + 1] - primes[i] > 90:
        print(primes[i], primes[i + 1])