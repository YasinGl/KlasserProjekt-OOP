import math

class GeometriskaFormer:
    def __init__(self, radie, bredd, höjd):
        self.radie = radie
        self.bredd = bredd
        self.höjd = höjd

    def cirkel_omkrets(self):
        return 2 * math.pi * self.radie

    def cirkel_area(self):
        return math.pi * self.radie ** 2

    def rektangel_omkrets(self):
        return 2 * (self.bredd + self.höjd)

    def rektangel_area(self):
        return self.bredd * self.höjd

    def visa_resultat(self):
        omkrets_cirkel = self.cirkel_omkrets()
        area_cirkel = self.cirkel_area()
        omkrets_rektangel = self.rektangel_omkrets()
        area_rektangel = self.rektangel_area()

        print(f"Omkrets för cirkeln är: {omkrets_cirkel}")
        print(f"Area för cirkeln är: {area_cirkel}")
        print(f"Omkrets för rektangeln är: {omkrets_rektangel}")
        print(f"Area för rektangeln är: {area_rektangel}")

# Läs in värden från användaren
radie = float(input("Skriv in radien för cirkeln: "))
bredd = float(input("Skriv in bredden för rektangeln: "))
höjd = float(input("Skriv in höjden för rektangeln: "))

# Skapa en instans av GeometriskaFormer-klassen
former = GeometriskaFormer(radie, bredd, höjd)

# Använd instansen för att beräkna och visa resultat
former.visa_resultat()
