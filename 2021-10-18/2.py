a, b = map(int, input().split())

ans = 0

for i in range(abs(b)):
    ans = ans + a

if b < 0:
    print(-ans)
else:
    print(ans)