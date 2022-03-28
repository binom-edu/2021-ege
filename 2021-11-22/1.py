def f(a, b, c):
    return (a and c) or ((not a) and (b or (not c)))


for a in range(2):
    for b in range(2):
        for c in range(2):
            if not f(a, b, c):
                print(a, b, c)