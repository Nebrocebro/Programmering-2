class Djur:
    def __init__(self, namn):
        self.namn = namn
    def ät(self):
        print("Ät!")
    def sov(self):
        print("Sov!")

class Fågel(Djur):
    def __init__(self, namn, vingspann):
        super().__init__(namn)
        self.vingspann = vingspann
        
class Fisk(Djur):
    def __init__(self, namn, maxdjup):
        super().__init__(namn)
        self.maxdjup = maxdjup
    def simma(self):
        print("Simma!")

class Haj(Fisk):
    def __init__(self, namn, maxdjup, antalTänder):
        super().__init__(namn, maxdjup)
        self.antalTänder = antalTänder
    def ät(djur):
        print("Äter djur!")

class Torsk(Fisk):
    def __init__(self, namn, maxdjup, hastighet):
        super().__init__(namn, maxdjup)
        self.hastighet = hastighet

def fånga(Haj, Torsk):
    if Haj.maxdjup >= Torsk.maxdjup and Torsk.hastighet < 30:
        return True
    
haj1 = Haj("tjena", 200, 150)
torsk1 = Torsk("mittbena", 200, 25)
fånga(haj1, torsk1)
haj1.simma()
torsk1.sov()
haj1.ät()