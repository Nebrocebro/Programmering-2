def calculate(a, b, d): 
    z = complex(a, b)
    k = z/d
    r = z%d
    print(r)

calculate(1, 5, 2)

# Heltalsdivision funkar men ej restdivision