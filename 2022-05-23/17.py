with open('17-5.txt') as file:
    a = [int(i) for i in file.read().splitlines()]

cnt = 0
smax = -10 ** 9

for i in range(len(a) - 1):
    if abs(a[i] )% 10 == 7 or abs(a[i + 1]) % 10 == 7:
        cnt += 1
        smax = max(smax, a[i] + a[i + 1])

print(cnt, smax)