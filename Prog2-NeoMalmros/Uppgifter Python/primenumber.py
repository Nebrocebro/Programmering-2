def primeCounter():
    i = 1
    k = 0
    l = 0
    while True:
        i += 1
        l = i + 1
        # is_prime = True
        is_prime_p1 = True
        is_prime_p2 = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                # is_prime = False
                is_prime_p1 = False
                break
        for m in range(2, int(l**0.5) + 1):
            if l % m == 0:
                is_prime_p2 = False
                break
        if is_prime_p1 and is_prime_p2:
            print(i, l)
            k += 1
            if len(str(i * l)) == 10:
                print(f'{i} * {l} är de två minsta primtalen vars produkt har 10 siffror')
                break
            else:
                continue
            # elif k == 1000:
            #     print(f'{i} är det tusende primtalet')
            #     break
            
primeCounter()