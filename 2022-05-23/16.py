def f(n):
    if n % 6 == 0:
        return 0
    if n <= 5:
        return n
    if n % 5 == 0:
        return n + f(n // 5 + 1)
    return n + f(n + 6)

n = 6
while f(n) <= 1000:
    n += 1

print(n)