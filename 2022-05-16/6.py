smin = None
for s1 in range(-1000, 1000):
    n = 1
    s = s1
    while s < 185:
        s = s + 30
        n = n * 3
    if n == 729:
        if smin == None:
            smin = s1
        smax = s1

print(smax, smin)