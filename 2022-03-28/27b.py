m2 = m3 = m6 = 0

with open('27b.txt') as fin:
    n = int(fin.readline())
    for i in range(n):
        t = int(fin.readline())
        if t % 6 == 0:
            m6 += 1
        elif t % 3 == 0:
            m3 += 1
        elif t % 2 == 0:
            m2 += 1

print(m6 * (n - m6) + m6 * (m6 - 1) // 2 + m2 * m3)