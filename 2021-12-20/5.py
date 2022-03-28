def dp(i, end):
    if i == end:
        return 1
    if i in frogs:
        return 0
    if i > end:
        return 0

    return dp(i + 1, end) + dp(i * 2, end)

frogs = [30, 15]
print(dp(1, 18) * dp(18, 40))