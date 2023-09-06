class Inköpslista:
    def __init__(self):
        self.inköpslista = []

    def lägg_till_objekt(self, objekt):
        self.inköpslista.append(objekt)

    def ta_bort_objekt(self, objekt):
        if objekt in self.inköpslista:
            self.inköpslista.remove(objekt)
        else:
            print(f"{objekt} finns inte i inköpslistan.")

    def visa_inköpslista(self):
        print("Inköpslista:")
        for objekt in self.inköpslista:
            print(objekt)

# Skapa en instans av Inköpslista-klassen
inköpslista = Inköpslista()

# Meny
while True:
    print("\nVälkommen till inköpslistan!")
    print("1. Lägg till objekt")
    print("2. Ta bort objekt")
    print("3. Visa inköpslistan")
    print("4. Avsluta")

    val = input("Välj en handling: ")

    if val == "1":
        objekt = input("Skriv in objekt att lägga till: ")
        inköpslista.lägg_till_objekt(objekt)
    elif val == "2":
        objekt = input("Skriv in objekt att ta bort: ")
        inköpslista.ta_bort_objekt(objekt)
    elif val == "3":
        inköpslista.visa_inköpslista()
    elif val == "4":
        print("Hej då!")
        break
    else:
        print("Ogiltigt val. Försök igen.")
