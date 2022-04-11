a  = []
with open('27-24b.txt') as fin:
    n = int(fin.readline())
    for i in range(n):
        a.append([int(i) for i in fin.readline().split()])

dp = [[-1 for i in range(n)] for j in range(3)]
dp[a[0][0] % 3][0] = a[0][0]
dp[a[0][1] % 3][0] = max([a[0][1] % 3][0], a[0][1])

for j in range(n - 1):
    for i in range(3):
        if dp[i][j] != -1:
            t = dp[i][j] + a[j + 1][0]
            dp[t % 3][j + 1] = max(dp[t % 3][j + 1], t)
            t = dp[i][j] + a[j + 1][1]
            dp[t % 3][j + 1] = max(dp[t % 3][j + 1], t)

print(max(dp[1][-1], dp[2][-1]))