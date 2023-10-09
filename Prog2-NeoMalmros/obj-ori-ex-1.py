import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius*2
    def calcCircle(self):
        try:
            self.area = round((self.radius**2)*math.pi)
            self.circumference = round(2*math.pi*self.radius)
            print(f"Radie: {self.radius}", f"Diameter: {self.diameter}", f"Omkrets: {self.circumference}", f"Area: {self.area}")
        except:
            print("Fel input")


cirkel1 = Circle(5)
cirkel1.calcCircle()

