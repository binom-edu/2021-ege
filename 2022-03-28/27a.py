with open('27a.txt') as fin:
    n = int(fin.readline())
    a = []
    for i in range(n):
        a.append(int(fin.readline()))

c = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] * a[j] % 6 == 0:
            c += 1

print(c)