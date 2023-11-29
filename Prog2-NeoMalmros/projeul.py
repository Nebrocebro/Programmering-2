import math

a = 0
b = 0
while a <= 1000:
    a += 1
    print("a ökar")
    while b <= 1000:
        b += 1
        print("b ökar")
        if (math.sqrt(a**2 + b**2)) % 2 == 0 and a + b + math.sqrt(
            a**2 + b**2
        ) == 1000:
            print(a * b * (math.sqrt(a**2 + b**2)))
        else:
            continue
