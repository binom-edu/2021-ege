def dp(i, end):
    if i == end:
        return 1
    if i == 30:
        return 0
    if i > end:
        return 0

    return dp(i + 1, end) + dp(i * 2, end)


print(dp(1, 18) * dp(18, 40))