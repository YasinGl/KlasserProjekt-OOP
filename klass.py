class raknare:
    def __int__(self):
     pass
    def lasnummber(self):
        self.tal1 = float(input("Ange det första talet: "))
        self.tal2 = float(input("Ange det andra talet: "))
    def kalkulera_total_tal(self):
        self.summa = self.tal1 + self.tal2

    def visa_result(self):
        print(f"Summan av {self.tal1} och {self.tal2} är {self.summa}")

raknare = raknare()
raknare.lasnummber()
raknare.kalkulera_total_tal()
raknare.visa_result()