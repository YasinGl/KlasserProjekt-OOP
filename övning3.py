import math

# Funktion för att beräkna omkretsen av en cirkel
def cirkel_omkrets(radie):
    return 2 * math.pi * radie

# Funktion för att beräkna arean av en cirkel
def cirkel_area(radie):
    return math.pi * radie ** 2

# Funktion för att beräkna omkretsen av en rektangel
def rektangel_omkrets(bredd, höjd):
    return 2 * (bredd + höjd)

# Funktion för att beräkna arean av en rektangel
def rektangel_area(bredd, höjd):
    return bredd * höjd

# Använd funktionerna för att beräkna omkrets och area av cirkeln
radie = float(input("Ange radien för cirkeln: "))
omkrets_cirkel = cirkel_omkrets(radie)
area_cirkel = cirkel_area(radie)

print(f"Cirkelns omkrets är: {omkrets_cirkel}")
print(f"Cirkelns area är: {area_cirkel}")

# Använd funktionerna för att beräkna omkrets och area av rektangeln
bredd = float(input("Ange bredden för rektangeln: "))
höjd = float(input("Ange höjden för rektangeln: "))
omkrets_rektangel = rektangel_omkrets(bredd, höjd)
area_rektangel = rektangel_area(bredd, höjd)

print(f"Rektangelns omkrets är: {omkrets_rektangel}")
print(f"Rektangelns area är: {area_rektangel}")
