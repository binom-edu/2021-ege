with open('/home/ak/prog/ege21/2022-03-07/26-39.txt') as fin:
    n, m = map(int, fin.readline().split())
    a = []
    for i in range(n):
        a.append(int(fin.readline()))

b = []
c = []
for i in a:
    if 180 <= i <= 200:
        b.append(i)
    else:
        c.append(i)

b.sort(reverse=True)

cnt = 0
weight = 0
for i in b:
    cnt += 1
    weight += i
    if weight > m:
        weight -= i
        cnt -= 1
        break

empty = m - weight
c.sort()
onboard = []

while sum(onboard) + c[0] <= empty:
    onboard.append(c.pop(0))

for i in range(len(onboard) - 1, -1, -1):
    c.append(onboard.pop(i))
    x = max([j for j in c if j <= empty - sum(onboard)])
    onboard.append(x)
    c.remove(x)

print(cnt + len(onboard), weight + sum(onboard))