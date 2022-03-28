def dp(i):
    if i == 1:
        return 1
    ans = dp(i - 1)
    if i % 2 == 0:
        ans += dp(i // 2)
    return ans

print(dp(20))