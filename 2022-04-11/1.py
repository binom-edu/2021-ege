a = []
with open('27.txt') as fin:
    n = int(fin.readline())
    for i in range(n):
        a.append(int(fin.readline()))

ans = -1
for i in range(n):
    for j in range(n):
        if j - i >= 6 and a[i] * a[j] > ans:
            ans = a[i] * a[j]

print(ans)