a = []
with open('27_B.txt') as fin:
    n = int(fin.readline())
    for i in range(n):
        a.append(int(fin.readline()))
maxS = 0
minLen = n
presum = [0] * n # префиксные суммы
s = 0 # текущая сумма
lefts = [None] * 43
rights = [None] * 43
lefts[0] = -1
for i in range(n):
    s += a[i]
    presum[i] = s
    t = s % 43
    if lefts[t] == None:
        lefts[t] = i
    rights[t] = i

for i in range(43):
    if lefts[i]:
        s = presum[rights[i]] - presum[lefts[i]]
        if s > maxS or s == maxS and rights[i] - lefts[i] < minLen:
            maxS = s
            minLen = rights[i] - lefts[i]
print(minLen)