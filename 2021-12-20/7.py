def dp(i, end):
    if i == end:
        return 1
    if i in frogs:
        return 0
    if i > end:
        return 0

    return dp(i + 1, end) + dp(i * 3, end) + dp(i * i, end)

frogs = [81]
print(dp(2, 100))