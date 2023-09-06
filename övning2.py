# Berätta för användaren vad programmet gör
print("Detta program ber dig att ange två tal och utför några beräkningar med dem.")

# Läs in två tal från användaren
tal1 = float(input("Ange det första talet: "))
tal2 = float(input("Ange det andra talet: "))

# Utför några beräkningar
summa = tal1 + tal2
produkt = tal1 * tal2
kvot = tal1 / tal2

# Visa resultatet
print(f"Summan av {tal1} och {tal2} är {summa}")
print(f"Produkten av {tal1} och {tal2} är {produkt}")
print(f"Kvoten av {tal1} och {tal2} är {kvot}")
