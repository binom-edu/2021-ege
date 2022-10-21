with open('/home/ak/prog/2021-ege/2022-06-05/27-65a.txt') as fin:
    n = int(fin.readline())
    a = []
    for i in range(n):
        t = [int(j) for j in fin.readline().split()]
        if t[1] % 2 == 0:
            continue
        a.append(sorted(t))

n = len(a)
ans = 0

def f(lst, i):
    global ans
    if i == n:
        s0 = sum([k[0] for k in lst])
        s1 = sum([k[1] for k in lst])
        if s1 % 2 == 0 and s0 % 2 != 0:
            ans = max(ans, s0 + s1)
        return
    f(lst, i + 1)
    lst1 = lst.copy()
    lst1.append(a[i])
    f(lst1, i + 1)

f([], 0)
print(ans)