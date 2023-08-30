x = 0
for i in range (0, 999):
    if i % 7 == 0:
        print(i)
        x += 1
    else:
        continue
print(f'Det finns {x} stycken tal under 1000 som är delbart med 7.')