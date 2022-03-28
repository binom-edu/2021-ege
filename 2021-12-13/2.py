# кузнечик с деньгами

n = int(input())
a = [int(i) for i in input().split()]

a = [None] + a

dp = [0] * (n + 1)
dp[0] = 0
dp[1] = a[1]

for i in range(2, n + 1):
    dp[i] = a[i] + max(dp[i - 1], dp[i - 2])

print(dp[n])