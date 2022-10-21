n = 4 ** 503 + 3 * 4 ** 244 - 2 * 4 ** 444 - 95
ans = 0
while n:
    if n % 4 == 3:
        ans += 1
    n //= 4

print(ans)