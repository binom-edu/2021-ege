with open('26-J1.txt') as fin:
    n = int(fin.readline())
    a = []
    for i in range(n):
        a.append(int(fin.readline()))

cnt = 0

f = [0] * 100
for i in a:
    f[i] += 1

for i in range(1, 50):
    cnt += min(f[i], f[100 - i])

cnt += f[50] // 2

print(cnt)