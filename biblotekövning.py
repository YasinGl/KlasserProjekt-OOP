class bibllotek:
    def __init__(self):
        self.Biblotek = []

    def lägg_till_(self, titel, författare):
        bok = {"titel": titel, "författare": författare}
        self.Biblotek.append(bok)

    def ta_bort(self,bok):
        if bok in self.Biblotek:
            self.Biblotek.remove(bok)

        else:
            print(f"Din bok {bok} finns ej hos oss")

    def kolla(self):
        print("Böcker inne: ")
        for bok in self.Biblotek:
            print(bok)

Biblotek = bibllotek()

while True:
    print("Välkommen till bibloteket!")
    print("1. Lägg till bok!")
    print("2. Ta bort bok")
    print("3. Lista över våra böcker")
    print("4. Ange titel och författer för att söka efter bok")
    print("5. Avsluta")

    val = input("Välj en handling: ")

    if val == "1":
        titel = input("Skriv in bokens titel: ")
        författare = input("Skriv in författarens namn: ")
        bibllotek.lägg_till_(titel, författare)

    elif val == "2":
        objekt = input("Skriv in bok att ta bort: ")
        bok.ta_bort(Biblotek)
    elif val == "3":
        bibllotek.kolla()
        if val == "4":
            titel = input("Skriv in titel att söka efter: ")
            författare = input("Skriv in författare att söka efter: ")
            hittade_böcker = []
            for bok in bibllotek.Biblotek:
                if bok["titel"] == titel and bok["författare"] == författare:
                    hittade_böcker.append(bok)
            if hittade_böcker:
                print("Hittade böcker:")
                for bok in hittade_böcker:
                    print(f'Titel: {bok["titel"]}, Författare: {bok["författare"]}')
            else:
                print("Ingen matchande bok hittades.")

    elif val == "5":
        print("Hej då!")
        break
    else:
        print("Ogiltigt val. Försök igen.")





