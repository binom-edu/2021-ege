dp = [None] * 70

def f(s1: int, s2: int) -> list:
    if s1 + s2 >= 77:
        return ['-', 0]
    if dp[s2] != None:
        return dp[s2]
    r = []
    r.append(f(s1 + 1, s2))
    r.append(f(s1 * 2, s2))
    r.append(f(s1, s2 + 1))
    r.append(f(s1, s2 * 2))
    win = [i[1] for i in r if i[0] == '-']
    lose = [i[1] for i in r if i[0] == '+']
    if len(win) > 0:
        return ['+', min(win) + 1]
    return ['-', max(lose)]


for s in range(1, 70):
    print(s, *f(7, s))