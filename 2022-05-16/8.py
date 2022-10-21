alf = 'ВАЙФУ'
cnt = 0

def f(s):
    global cnt
    if len(s) == 4:
        if s[0] != 'Й' and (not 'ВФ' in s) and (not 'ФВ' in s):
            cnt += 1
        return
    for i in alf:
        if not i in s:
            f(s + i)

f('')
print(cnt)