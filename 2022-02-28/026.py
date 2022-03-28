with open('26.txt') as fin:
    s, n = map(int, fin.readline().split())
    a = []
    for i in range(n):
        a.append(int(fin.readline()))

a.sort()
b = []
for i in a:
    if sum(b) + i <= s:
        b.append(i)
    else:
        break
ans1 = len(b)
empty = s - (sum(b) - b[-1])
ans2 = max([i for i in a if i <= empty])
print(ans1, ans2)