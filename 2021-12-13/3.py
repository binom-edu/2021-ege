# кузнечик с деньгами и лягушками

n = int(input())
a = [int(i) for i in input().split()]
frogs = [int(i) for i in input().split()]

a = [None] + a

INF = -10 ** 9
for i in frogs:
    a[i] = INF

dp = [0] * (n + 1)
dp[0] = 0
dp[1] = a[1]

for i in range(2, n + 1):
    dp[i] = a[i] + max(dp[i - 1], dp[i - 2])

if dp[n] < -10 ** 7:
    print('oh no')
else:
    print(dp[n])

print(dp)