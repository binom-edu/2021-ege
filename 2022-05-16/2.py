def f(w, x, y, z):
    return (w <= y) and ((x <= z) == (y <= x))

print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if f(w, x, y, z):
                    print(w, x, y, z)