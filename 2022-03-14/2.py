with open('26-k6.txt') as fin:
    n, k = map(int, fin.readline().split())
    a = []
    for i in range(n):
        w, p = map(int, fin.readline().split())
        a.append([w, p])

a.sort(key=lambda x: [x[1] / x[0], -x[0]])

b = a[:k]

print(sum([i[0] for i in b]))
print(max(b)[1])
