abc = 'лето'
cnt = 0
lst = []

def f(s):
    global cnt
    if len(s) == 4:
        if s[0] == 'л' or s[0] == 'т':
            cnt += 1
        return
    for i in abc:
        f(s + i)

f('')
print(cnt)