def add_this(*args):
    calculate = 0
    print("Alla talen:")
    for x in args:
        print(x)
        calculate += x
    print("Talens summa:", calculate)

add_this(2, 3, 4, 5, 56)
add_this(2, 3, 5)