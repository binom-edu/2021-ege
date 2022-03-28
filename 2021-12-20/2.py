def dp(i):
    if i == 20:
        return 1
    if i > 20:
        return 0

    return dp(i + 1) + dp(i * 2)

print(dp(1))