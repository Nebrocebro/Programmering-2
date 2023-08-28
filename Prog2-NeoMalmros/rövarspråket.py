civiliserat = input("Skriv din mening här:")
konsonanter = "bcdfghjklmnpqrstvwxz"
def rövning(string):
    for i in konsonanter:
        string = string.replace(i, i + "o" + i)
    print(string)
rövning(civiliserat)