i = 2
k = 0
for i in range():
    i += 1
    for k in range():
        if i % 1 == 0 and i % i == 0:
            for j in range(int(i/2), i):
                j += 1
                if i % j == 0:
                    break
                elif i == j:
                    print(f'{i} är ett primtal!')
                    k += 1
                    break
                else:
                    continue
        if k == 1000:
            print(f'{i} är det tusende primtalet')
            break