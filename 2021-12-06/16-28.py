def f(n, s):
    if n >= 4 and dp[n] != None:
        return dp[n]
    s += 2 * n + 1
    # print(2 * n + 1)
    if n > 1:
        s += 3 * n - 8
        # print(3 * n - 8)
        f(n - 1, s)
        f(n - 4, s)
    dp[n] = s
    return s

dp = [None] * 10000000
i = 1
while True:
    if f(i, 0) > 5000000:
        print(i, f(i, 0))
        break
    i += 1