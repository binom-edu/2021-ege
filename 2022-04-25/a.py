a = []

with open('27_A.txt') as fin:
    n = int(fin.readline())
    for i in range(n):
        a.append(int(fin.readline()))

maxS = 0
minLen = n

for i in range(n):
    for j in range(i, n):
        s = sum(a[i: j + 1])
        if s % 43 == 0:
            if s > maxS:
                maxS = s
                minLen = j - i + 1
            elif s == maxS and j - i + 1 < minLen:
                minLen = j - i + 1
print(minLen)