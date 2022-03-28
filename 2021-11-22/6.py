for y in range(1, 1000):
    x = y
    flag = True
    while x < 100:
        if x % 2 < 1:
            x = x // 2
        else:
            x = 3*x + 1
        if x == 1:
            flag = False
            break
    if flag:
        print(y)