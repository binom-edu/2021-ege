def f(s: int) -> list :
    if s > 28:
        return ['-', 0]
    r1 = f(s + 1)
    r2 = f(s * 2)
    wins = []
    fails = []
    if r1[0] == '-':
        wins.append(r1[1])
    else:
        fails.append(r1[1])
    if r2[0] == '-':
        wins.append(r2[1])
    else:
        fails.append(r2[1])
    if wins:
        return ['+', min(wins) + 1]
    return ['-', max(fails)]

for i in range(1, 29):
    print(i, ':', *f(i))