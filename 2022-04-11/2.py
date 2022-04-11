a = []
with open('27b.txt') as fin:
    n = int(fin.readline())
    for i in range(n):
        a.append(int(fin.readline()))

m = a.copy()
for i in range(n - 2, -1, -1):
    m[i] = max(m[i], m[i + 1])

ans = -1
for i in range(n - 6):
    ans = max(ans, a[i] * m[i + 6])
    
print(ans)