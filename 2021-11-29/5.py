n = int(input())
a = b = 1
for i in range(3, n + 1):
    a, b = b, a + b
print(b)