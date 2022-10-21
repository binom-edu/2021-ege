with open('26-46.txt') as fin:
    a = []
    n = int(fin.readline())
    for i in range(n):
        a.append(int(fin.readline()))

cnt = 0
avmin = 10**9
s = set(a)

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if (a[i] + a[j] + a[k]) % 3 == 0 and (a[i] + a[j] + a[k]) // 3 in s:
                cnt += 1
                avmin = min(avmin, (a[i] + a[j] + a[k]) // 3)
print(cnt, avmin)