#-------------------------------------------------------------
# for-Schleife
#
#Autor:   Dein Name
#Datum:   Aktuelles Datum
#-------------------------------------------------------------

# Eingabe der Zählwerte
Startwert = int(input("Startwert des Zählers: "))
Endwert = int(input("Endwert des Zählers: "))
Schrittweite = int(input("Schrittweite des Zählers: "))

# Zählwerte durchlaufen
for i in range(Startwert, Endwert, Schrittweite):
    print(i)