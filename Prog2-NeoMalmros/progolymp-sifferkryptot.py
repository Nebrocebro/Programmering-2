decipherDict = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E',
    6: 'F',
    7: 'G',
    8: 'H',
    9: 'I',
    10: 'J',
    11: 'K',
    12: 'L',
    13: 'M',
    14: 'N',
    15: 'O',
    16: 'P',
    17: 'Q',
    18: 'R',
    19: 'S',
    20: 'T',
    21: 'U',
    22: 'V',
    23: 'W',
    24: 'X',
    25: 'Y',
    26: 'Z',
    27: 'Å',
    28: 'Ä',
    29: 'Ö'
}

crypticString = int(input("Skriv upp till 15 siffror utan mellanslag"))
decipheredWord = {}

def decipherCode():
    crypticList = crypticString.split()
    for i in crypticList:
        decipheredWord += decipherDict.get(crypticList(i))
        if i == len(crypticList):
            print(decipheredWord)
            break
        
decipherCode()