#-------------------------------------------------------------
# Aufruf continue in while-Schleife
#
#Autor:   Dein Name
#Datum:   Aktuelles Datum
#-------------------------------------------------------------

zaehler = 0

# Von 1 bis 10 zählen
while zaehler <= 10:
	zaehler += 1

# Ungerade Zahlen ignorieren
if zaehler % 2:
	continue # Alles ab hier wird übersprungen

	print("Zähler: ", zaehler))