text = input('Skriv en text med bokstäver och siffror.')
k = 0
lst = []
def check(string):
    for char in text:
        lst.append(char)
        if lst[k].isnumeric():
            print(k.value)
            k += 1
        elif lst[k] == text[len]:
            print(k)
            break

check(text)

            # isnumeric, for char