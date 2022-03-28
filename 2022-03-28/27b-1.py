m2 = m3 = m6 = c = 0

with open('27b.txt') as fin:
    n = int(fin.readline())
    for i in range(n):
        t = int(fin.readline())
        if t % 6 == 0:
            m6 += 1
            c += i
        elif t % 3 == 0:
            m3 += 1
            c += m2 + m6
        elif t % 2 == 0:
            m2 += 1
            c += m3 + m6
        else:
            c += m6

print(c)