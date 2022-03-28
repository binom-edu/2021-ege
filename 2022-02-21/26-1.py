with open('26-s1.txt') as fin:
    n = int(fin.readline())
    a = []
    for i in range(n):
        a.append(int(fin.readline()))

sales = [i for i in a if i > 100]
sales.sort()
n1 = len(sales)
discount = int(sum(sales[:n1 // 2]) * 0.1)
print(sum(a) - discount, sales[n1 // 2 - 1])