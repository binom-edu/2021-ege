def countOfDigits(x):
    s = str(x)
    return len(s)

def isValid(x):
    xcopy = x
    l = countOfDigits(x)
    result = 0
    while x > 0:
        d = x % 10
        result += d ** l
        x //= 10
    return result == xcopy


a, b = map(int, input().split())

ans = []

for i in range(a, b + 1):
    if isValid(i):
        ans.append(i)

if len(ans) > 0:
    print(*ans)
else:
    print(-1)