#-------------------------------------------------------------
# elif-Bedingung für den Geldautomaten
#
#Autor:   Dein Name
#Datum:   Aktuelles Datum
#-------------------------------------------------------------

# Menü ausgeben
print("Sie können folgende Beträge abheben:")
print("1: 50 €\n2: 100 €")
print("3: 200 €\n4: 500 €")

# Gewünschte Aktion abfragen
aktion = int(input("Wählen Sie eine Aktion (1-4): "))

# Funktion ausführen
if aktion == 1:
    print("Bitte warten. Die 50 € werden gleich bereitgestellt. #Knauser")
elif aktion == 2:
    print("Bitte warten. Die 100 € werden gleich bereitgestellt.")
elif aktion == 3:
    print("Bitte warten. Die 200 € werden gleich bereitgestellt.")
elif aktion == 4:
    print("Bitte warten. Die 500 € werden gleich bereitgestellt. #DickesPortmonee")
else:
    print("Ungültige Aktion! Abbruch")