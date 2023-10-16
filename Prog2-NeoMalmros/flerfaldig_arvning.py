class Landdjur:
    def __init__(self, kanGå):
        self.kanGå = kanGå
    def andas(self):
        print("Jag kan kanske gå?")

class Havsdjur:
    def __init__(self, simHastighet):
        self.simHastighet = simHastighet
    def simma(self):
        print("Jag kan simma!")

class Däggdjur():
    def __init__(self, mjölkBehov, literLuft):
        self.mjölkBehov = mjölkBehov
        self.literLuft = literLuft

class Fisk(Havsdjur):
    def __init__(self, simHastighet, literVatten, antalGälar):
        Havsdjur.__init__(simHastighet)
        self.antalGälar = antalGälar
        self.literVatten = literVatten
    def andasVatten(self):
        print("Jag andas i vattnet!")

class Ödla(Landdjur):
    def __init__(self, kanGå, antalFjäll):
        Landdjur.__init__(kanGå)
        self.antalFjäll = antalFjäll
    def klättra(self):
        print("Jag kan klättra på väggar!")

class Häst(Landdjur, Däggdjur):
    def __init__(self, kanGå, mjölkBehov, literLuft, maxHastighet):
        Landdjur.__init__(kanGå)
        Däggdjur.__init__(mjölkBehov, literLuft)
        self.maxHastighet = maxHastighet
    def spring(self):
        print("Jag kan springa fort!")

class Val(Havsdjur, Däggdjur):
    def __init__(self, simHastighet, kiloPlankton):
        Havsdjur.__init__(simHastighet)
        self.kiloPlankton = kiloPlankton
    def svälj(self):
        print(f"Jag kan äta {self.kiloPlankton} kilo plankton varje dag!")