class Human:
    def __init__(self, strength, name):
        self.strength = strength
        self.name = name

class Orc:
    def __init__(self, poisonLevel):
        self.poisonLevel = poisonLevel

class Hobbit:
    def __init__(self, height):
        self.height = height

class Warrior:
    def __init__(self, weaponLevel):
        self.weaponLevel = weaponLevel

    def slå(self):
        print(f"Du slår med en kraft av {self.weaponLevel} kg!")

class Mage:
    def __init__(self, manaLevel):
        self.manaLevel = manaLevel

    def vaporize(self):
        print(f"Du vaporiserar din fiende med {self.manaLevel} MN av energi!")

class Thief:
    def __init__(self, pickpocketLevel):
        self.pickpocketLevel = pickpocketLevel

    def steal(self):
        print(f"Du lyckas stjäla {self.pickpocketLevel} tusen kronor!")

class HumanWarrior(Human, Warrior):
    def __init__(self, strength, weaponLevel, name):
        Human.__init__(self, strength, name)
        Warrior.__init__(self, weaponLevel)

    def strengthMeter(self):
            print(f"Du har {self.strength * self.weaponLevel} kg av kraft bakom dina slag!")

    def statisticsHuWa(self):
        print(f"Hej {self.name}! Här är din statistik:")
        print(f"Du har {self.strength} i styrka!")
        print(f"Du har {self.weaponLevel} i vapennivå!")
        self.strengthMeter()

newWarrior = HumanWarrior(50, 25, "Joe")
newWarrior.statisticsHuWa()
newWarrior2 = HumanWarrior(5, 150, "Mama")
newWarrior2.statisticsHuWa()