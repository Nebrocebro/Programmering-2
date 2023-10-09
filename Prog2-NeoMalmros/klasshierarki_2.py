class Fordon:
    def kör(self):
        print("Nu kör vi!")
class Bil(Fordon):
    def tuta(self):
        print("Tuuut!!")
class Cykel(Fordon):
    def ring(self):
        print("Ring ring jag är en cyklist och kör in i dig om inte du flyttar dig!")
b = Bil()
b.kör()     # anropar en Fordon-metod i ett Bil-objekt
b.tuta()    # anropar en Bil-metod
c = Cykel()
c.ring()