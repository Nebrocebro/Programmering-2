class Elev:
    def __init__(self, namn, ålder, godkänd):
        self.namn = namn
        self.ålder = ålder
        def happyCheck():
            if godkänd == True:
                self.glad = True
        happyCheck()
        def presentera():
            print("Hej jag heter", self.namn)
        presentera()
        def presentera__ålder():
            print("Jag är", self.ålder, "år gammal")
        presentera__ålder()

Elev1 = Elev("Markus Petterson", 673, True)