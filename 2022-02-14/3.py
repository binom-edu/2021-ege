# Ходы: -1, делить на 2, если s четно. проигрывает тот, кто взял последний камень
def f(s: int) -> list :
    if s == 0:
        return ['+', 0]
    r = []
    r.append(f(s - 1))
    if s % 2 == 0:
        r.append(f(s // 2))
    wins = [i[1] for i in r if i[0] == '-']
    fails = [i[1] for i in r if i[0] == '+']
    if wins:
        return ['+', min(wins)]
    return ['-', max(fails) + 1]

for i in range(1, 51):
    print(i, ':', *f(i))