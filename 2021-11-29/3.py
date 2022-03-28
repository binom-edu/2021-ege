def f(x):
    if a[x] != None:
        return a[x]
    
    res = f(x - 1) + f(x - 2)
    a[x] = res
    return res

n = int(input())
a = [None] * (n + 1)
a[1] = a[2] = 1
print(f(n))