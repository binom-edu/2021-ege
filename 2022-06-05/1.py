with open('input.txt') as fin:
    s = fin.read()

alf = 'ABC'
ans = 0
n = len(s)
for c in alf:
    pos = []
    for i in range(n):
        if s[i] == c:
            pos.append(i)
    for i in range(len(pos) - 1):
        ans = max(ans, pos[i + 1] - pos[i] + 1)

print(ans)