# Inköpslista
inköpslista = []

# Lägg till ett objekt i inköpslistan
def lägg_till_objekt(objekt):
    inköpslista.append(objekt)

# Ta bort ett objekt från inköpslistan
def ta_bort_objekt(objekt):
    if objekt in inköpslista:
        inköpslista.remove(objekt)
    else:
        print(f"{objekt} finns inte i inköpslistan.")

# Visa inköpslistan
def visa_inköpslista():
    print("Inköpslista:")
    for objekt in inköpslista:
        print(objekt)

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
        lägg_till_objekt(objekt)
    elif val == "2":
        objekt = input("Skriv in objekt att ta bort: ")
        ta_bort_objekt(objekt)
    elif val == "3":
        visa_inköpslista()
    elif val == "4":
        print("Hej då!")
        break
    else:
        print("Ogiltigt val. Försök igen.")
