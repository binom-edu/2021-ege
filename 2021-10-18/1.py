n = int(input())

for i in range(2, n):
    if n % i == 0:
        print('composite')
        break
    if i * i > n:
        print('prime')
        break
else:
    print('prime')