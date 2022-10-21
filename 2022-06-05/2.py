with open('24-164.txt') as fin:
    a = fin.read().splitlines()

ans = 0
alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for s in a:
    if s.count('E') >= 20:
        continue
    for c in alf:
        ans = max(ans, s.rfind(c) - s.find(c))

print(ans)