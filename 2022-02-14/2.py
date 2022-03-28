def f(s: int) -> list :
    if s > 49:
        return ['-', 0]
    r = []
    r.append(f(s + 1))
    r.append(f(s * 3))
    wins = [i[1] for i in r if i[0] == '-']
    fails = [i[1] for i in r if i[0] == '+']
    if wins:
        return ['+', min(wins) + 1]
    return ['-', max(fails)]

for i in range(1, 49):
    print(i, ':', *f(i))