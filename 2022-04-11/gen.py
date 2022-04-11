import random
with open('27b.txt', 'w') as fout:
    fout.write('999000\n')
    for i in range(999000):
        fout.write(str(random.randint(0, 10 ** 9)) + '\n')