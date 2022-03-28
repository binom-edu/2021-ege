from math import sqrt
def dp(start, i):
    if i == start:
        return 1
    if i < start:
        return 0
    if i in frogs:
        return 0
    if a[i] != None:
        return a[i]

    ans = dp(start, i - 1)
    if i % 3 == 0:
        ans += dp(start, i // 3)
    if i in [4, 9, 16, 25, 36, 49, 64, 81, 100]:
        ans += dp(start, int(sqrt(i)))
    a[i] = ans
    return ans

a = [None] * 101
frogs = [81]
print(dp(2, 100))