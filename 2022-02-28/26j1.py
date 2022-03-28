with open('26-J1.txt') as fin:
    n = int(fin.readline())
    a = []
    for i in range(n):
        a.append(int(fin.readline()))

cnt = 0
while a:
    t = a.pop()
    if 100 - t in a:
        i = a.index(100 - t)
        cnt += 1
        a.pop(i)

print(cnt)