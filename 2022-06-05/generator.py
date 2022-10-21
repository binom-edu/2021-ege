import random
with open('input.txt', 'w') as fout:
    alf = 'ABC'
    n = 10 ** 6
    for i in range(n):
        fout.write(random.choice(alf))

