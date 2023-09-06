class Elev:
    def __init__(self, namn, ålder, godkänd):
        self.namn = namn
        self.ålder = ålder
        if godkänd == True:
            self.glad = True
        def presentera():
            print("Hej jag heter", self.namn)
        presentera()

Elev1 = Elev("Markus Petterson", 673, True)