#-------------------------------------------------------------
# Rechnen mit Variablen und formatierte Ausgabe
#
#Autor:   Dein Name
#Datum:   Aktuelles Datum
#-------------------------------------------------------------
dollarkurs = input("Bitte aktuellen Dollarkurs eingeben: ")

kapital_in_euro = input("Bitte Kapital in Euro eingeben: ")

kapital_in_dollar = float(kapital_in_euro) * float(dollarkurs)

# Bisherige Vorgehensweise:
print(kapital_in_euro, "€ entsprechen", kapital_in_dollar, "$")

# Ausgabe mit der .format-Funktion:
vorlage = "{0} € entsprechen {1} $"
ausgabe = vorlage.format(kapital_in_euro, kapital_in_dollar)
print(ausgabe)

# Es funktioniert auch ohne Zwischenvariablen:
print("{0} € entsprechen {1} $".format(kapital_in_euro, kapital_in_dollar))

# Final die Variante von Maxx:
