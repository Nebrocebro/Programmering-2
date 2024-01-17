class Bil:
    __maxHastighet = 0
    antalBilar = 0
    def setMaxHastighet(self, maxHastighet):
        if type(maxHastighet) == int and maxHastighet > 0:
            self.__maxHastighet = maxHastighet
        else:
            print("Skriv ett positivt heltal")
    def getWeight(self):
        return self.__maxHastighet
    @staticmethod
    def milestokm(miles):
        return 1.6093*miles
    def __init__(self):
        antalBilar += 1

