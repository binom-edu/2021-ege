a = []
with open('27b.txt') as fin:
    n = int(fin.readline())
    for i in range(n):
        a.append(int(fin.readline()))

m = a[0]
ans = -1
buf = a[1:6]
for i in range(6, n):
    ans = max(ans, a[i] * m)
    m = max(m, buf.pop(0))
    buf.append(a[i])
    
print(ans)