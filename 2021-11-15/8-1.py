s = 'елмру'
i = 1
for a1 in s:
    for a2 in s:
        for a3 in s:
            for a4 in s:
                if a1 == 'л':
                    print(i)
                    exit()
                i += 1