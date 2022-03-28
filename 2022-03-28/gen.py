import random
with open('27b.txt', 'w') as f:
    f.write('1000000\n')
    for i in range(10 ** 6):
        f.write(str(random.randint(1, 1000)) + '\n')
