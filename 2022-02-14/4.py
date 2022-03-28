# Ходы: -1, любое четное кол-во. проигрывает тот, кто взял последний камень

a = [None] * 52

def f(s: int) -> list :
    if s == 0:
        return ['+', 0]
    if a[s] != None:
        return a[s]
    r = []
    r.append(f(s - 1))
    i = 1
    while 2 * i <= s:
        r.append(f(s - 2 * i))
        i += 1
    wins = [i[1] for i in r if i[0] == '-']
    fails = [i[1] for i in r if i[0] == '+']
    if wins:
        a[s] = ['+', min(wins)]
        return a[s]
    a[s] = ['-', max(fails) + 1]
    return a[s]

for i in range(1, 51):
    print(i, ':', *f(i))