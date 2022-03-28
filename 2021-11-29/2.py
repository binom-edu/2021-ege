for i in range(1, 10000):
    x = i
    a = 3 * x + 19
    b = 3 * x - 21
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    if a == 20:
        print(i)
        break