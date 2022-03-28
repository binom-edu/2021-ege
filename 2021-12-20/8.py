n = int(input())
dp = [None] * (n + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 4
dp[5] = 1
dp[6] = 1
for i in range(7, n + 1):
    dp[i] = min(dp[i - 1],
                dp[i - 5],
                dp[i - 6]) + 1
print(dp[-1])