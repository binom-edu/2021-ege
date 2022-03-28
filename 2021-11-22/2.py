def f(x, y, z):
    return (not x or y) and (not y or z)

print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if f(x, y, z):
                print(x, y, z)