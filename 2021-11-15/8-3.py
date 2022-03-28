import itertools
cnt = 0
for i in itertools.combinations_with_replacement('лето', 4):
    if i[0] == 'л' or i[0] == 'т':
        print(i)
        cnt += 1

print(cnt)