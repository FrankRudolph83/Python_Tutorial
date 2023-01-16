#-------------------------------------------------------------
# Aufruf else in while-Schleife
#
#Autor:   Dein Name
#Datum:   Aktuelles Datum
#-------------------------------------------------------------

# Abfragen, wann Zähler beendet werden soll
Abbruchkriterium = int(input("Abbruch der Additon bei: "))
Additionswert = 0

# Bis zehn zählen oder Abbruchkriterium
while Additionswert <= 10:
	if Additionswert == Abbruchkriterium:
	print("Zähler abgebrochen")
	break

	Additionswert += 1
else:
	print("Zähler erfolgreich beendet!")