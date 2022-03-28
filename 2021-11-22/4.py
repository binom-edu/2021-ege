for d in range(1, 100):
    n = 3
    s = 57
    while s <= 1200:
        s = s + d
        n = n + 4
    if n == 63:
        print(d)
        break