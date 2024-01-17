# global antalMorötter = 40
# global torMorötter = 0
# global morMorötter = 0

# def eatingContest():
#     torTime = int(input("Skriv Tors tid per morot"))
#     a = torTime
#     morTime = int(input("Skriv Mors tid per morot"))
#     b = morTime

#     torMorötter += 1
#     morMorötter += 1

#     while antalMorötter >= 1:
#         if antalMorötter == 1:
#             gameOver()
#             break
#         else:
#             torTime -= 1
#             morTime -= 1
#         if torTime == 0:
#             torMorötter += 1
#             antalMorötter -= 1
#             torTime == a
#         if morTime == 0:
#             morMorötter += 1
#             antalMorötter -= 1
#             morTime == b
        
# def gameOver():
#     print(f"Tors morötter var: {torMorötter} med tiden {a}")
#     print(f"Mors morötter var: {morMorötter} med tiden {b}")

# eatingContest()

def gameOver():
    print(f"Tors morötter var: {torMorötter} med tiden {a}")
    print(f"Mors morötter var: {morMorötter} med tiden {b}")

def eatingContest():
    global torMorötter, morMorötter, a, b
    antalMorötter = 40
    torMorötter = 0
    morMorötter = 0
    torTime = int(input("Skriv Tors tid per morot: "))
    a = torTime
    morTime = int(input("Skriv Mors tid per morot: "))
    b = morTime

    torMorötter += 1
    morMorötter += 1
    antalMorötter -= 2

    while antalMorötter >= 1:
        if antalMorötter == 1 and torTime == 0 and morTime == 0 or torMorötter + morMorötter == 40:
            break
        else:
            torTime -= 1
            morTime -= 1
        if torTime == 0:
            torMorötter += 1
            antalMorötter -= 1
            torTime = a
        if morTime == 0:
            morMorötter += 1
            antalMorötter -= 1
            morTime = b
    gameOver()

eatingContest()
