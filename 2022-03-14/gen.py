import random
with open('1.txt', 'w') as fout:
    fout.write('500 20\n')
    for i in range(20):
        w = random.randint(1, 10)
        p = random.randint(10, 100)
        fout.write(f'{w} {p}\n')