# кузнечик с лягушками

n = int(input())
frogs = [int(i) for i in input().split()]

dp = [0] * (n + 1)
dp[0] = dp[1] = 1

for i in range(2, n + 1):
    if i in frogs:
        dp[i] = 0
    else:
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])