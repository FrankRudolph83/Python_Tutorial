#-------------------------------------------------------------
# Aufruf break in while-Schleife
#
#Autor:   Dein Name
#Datum:   Aktuelles Datum
#-------------------------------------------------------------

# Menü ausgeben
print("Sie können folgende Beträge abheben:")
print("1: 50 €\n2: 100 €")
print("3: Geld sparen und beenden")

# Gewünschte Aktion abfragen
while True:
	aktion = int(input("Aktion wählen: "))

	# Funktion ausführen
	if aktion == 1:
		print("Bitte warten. Die 50 € werden gleich bereitgestellt.")
	elif aktion == 2:
		print("Bitte warten. Die 100 € werden gleich bereitgestellt.")
	elif aktion == 3:
		print("Sparen, sparen, sparen!")
		break
	else:
		print("Ungültige Eingabe")

print("Adieu, ihr Kassenautomat")