abc = 'крант'
cnt = 0

def f(s: str):
    global cnt
    if len(s) == 5:
        if s.count('к') == 2:
            cnt += 1
        return
    for i in abc:
        f(s + i)

f('')
print(cnt)