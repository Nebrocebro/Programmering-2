antalMorötter = 40
torMorötter = 0
morMorötter = 0
def eatingContest():
    a = int(input("Skriv Tors tid per morot"))
    b = int(input("Skriv Mors tid per morot"))
    if a < b:
        ratio = a/b
    elif a > b:
        ratio = b/a
    if antalMorötter == 40:
        torMorötter += 1
        morMorötter += 1
    
    for i in range(1, 40):
        39/ratio 