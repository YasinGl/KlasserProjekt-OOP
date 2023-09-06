class barakna:
    def __init__(self, tal1, tal2):
        self.tal1 = tal1
        self.tal2 = tal2
    def raknaS(self):
        self.summa = self.tal1 + self.tal2

    def raknaP(self):
        self.summa2 = self.tal1 * self.tal2

    def raknaK(self):
        self.summa3 = self.tal1 / self.tal2

    def visa_result(self):
        print(f"Summan av två talan är {self.summa} Produkt av dom två talen är {self.summa2} , Delat på dom två talen är {self.summa3}")


tal1 = float(input("Mata in ditt tal"))
tal2 = float(input("Mata in ditt tal"))

Barakna = barakna(tal1,tal2)
Barakna.raknaS()
Barakna.raknaP()
Barakna.raknaK()
Barakna.visa_result()
