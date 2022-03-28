with open('1.txt') as fin:
    n, m = map(int, fin.readline().split())
    a = []
    for i in range(m):
        w, p = map(int, fin.readline().split())
        a.append([w, p])

a.sort(key=lambda x: x[1] / x[0])

cart = []
shop = []
for i in a:
    if i[1] <= n:
        cart.append(i)
        n -= i[1]
    else:
        shop.append(i)
        
b = [i for i in shop if i[1] <= n]
if b:
    cart.append(max(b))

print(sum(i[0] for i in cart))
print(n)