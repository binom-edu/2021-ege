a = []
with open('27_B.txt') as fin:
    n = int(fin.readline())
    for i in range(n):
        a.append(int(fin.readline()))
maxS = 0
minLen = n
s = 0
r = [None] * 43
r[0] = 0
rlen = [0] * 43
for i in range(n):
    s += a[i]
    t = s % 43
    if r[t]:
        if s - r[t] > maxS or s - r[t] == maxS and i - rlen[t] + 1 < minLen:
            maxS = s - r[t]
            minLen = i - rlen[t] + 1
    else:
        r[t] = s
        rlen[t] = i + 1
print(minLen)